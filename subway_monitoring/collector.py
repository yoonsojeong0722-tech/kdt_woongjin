import os
import requests
import psycopg2
from psycopg2.extras import execute_values
from datetime import datetime
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

API_KEY = os.getenv("SUBWAY_API_KEY", "sample")
DATABASE_URL = os.getenv("DATABASE_URL")

# API Configuration
BASE_URL = "http://swopenapi.seoul.go.kr/api/subway"
SERVICE = "realtimePosition"
TYPE = "json"

# List of lines to monitor (Standard Lines + Others)
# Adding a few major lines for initial monitoring. Can be expanded.
TARGET_LINES = [
    "1호선", "2호선", "3호선", "4호선", "5호선", "6호선", "7호선", "8호선", "9호선",
    "경의중앙선", "공항철도", "경춘선", "수인분당선", "신분당선", "우이신설선"
]

def fetch_realtime_data(line_name):
    """
    Fetch real-time position data for a specific line.
    """
    # Requesting 0 to 100 items (assuming usually < 100 trains per line at once)
    # If total count > 100, might need paging, but realtimePosition usually fits in one batch per line or allows large request.
    start_index = 0
    end_index = 100
    
    # URL Encoding for line name might be handled by requests, but let's be safe.
    url = f"{BASE_URL}/{API_KEY}/{TYPE}/{SERVICE}/{start_index}/{end_index}/{line_name}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if "realtimePositionList" in data:
            return data["realtimePositionList"]
        else:
            if "RESULT" in data:
                 print(f"Info for {line_name}: {data['RESULT']['MESSAGE']}")
            return []
            
    except Exception as e:
        print(f"Error fetching data for {line_name}: {e}")
        return []

def parse_and_insert(conn, raw_data):
    """
    Parse raw API data and insert into the database.
    """
    if not raw_data:
        return

    query = """
        INSERT INTO realtime_subway_positions (
            line_id, line_name, station_id, station_name, train_number,
            last_received_date, last_received_time, direction_type,
            destination_station_id, destination_station_name, train_status_code,
            is_express, is_last_train
        ) VALUES %s
    """
    
    values = []
    for item in raw_data:
        try:
            # Map fields
            recptn_dt = item.get("recptnDt") 
            # API returns generic date string, sometimes needs parsing or is DB compatible directly if ISO.
            # Seoul API usually returns '2024-01-01 12:00:00'. Postgres TIMESTAMP handles this fine.
            
            row = (
                item.get("subwayId"),
                item.get("subwayNm"),
                item.get("statnId"),
                item.get("statnNm"),
                item.get("trainNo"),
                item.get("lastRecptnDt"),
                recptn_dt,
                int(item.get("updnLine")) if item.get("updnLine").isdigit() else 0,
                item.get("statnTid"),
                item.get("statnTnm"),
                int(item.get("trainSttus")) if item.get("trainSttus") and item.get("trainSttus").isdigit() else None,
                True if item.get("directAt") == "1" or item.get("directAt") == "7" else False,
                True if item.get("lstcarAt") == "1" else False
            )
            values.append(row)
        except Exception as e:
            print(f"Error parsing item {item}: {e}")

    if values:
        with conn.cursor() as cur:
            execute_values(cur, query, values)
            conn.commit()
        print(f"Inserted {len(values)} records.")

def main():
    if not DATABASE_URL:
        print("Error: DATABASE_URL is not set in .env")
        return

    try:
        conn = psycopg2.connect(DATABASE_URL)
        print("Connected to Database.")
    except Exception as e:
        print(f"Database connection failed: {e}")
        return

    try:
        total_records = 0
        for line in TARGET_LINES:
            print(f"Fetching {line}...")
            data = fetch_realtime_data(line)
            if data:
                parse_and_insert(conn, data)
                total_records += len(data)
            # Sleep briefly to avoid hitting rate limits if any
            time.sleep(0.5)
            
        print(f"Job Initialized. Total records inserted: {total_records}")

    finally:
        conn.close()
        print("Database connection closed.")

if __name__ == "__main__":
    main()
