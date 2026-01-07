import os
import requests
import json
from dotenv import load_dotenv

# Load env vars from the current directory
load_dotenv()

API_KEY = os.getenv("SUBWAY_API_KEY")
if not API_KEY or API_KEY == "sample":
    # Fallback if .env isn't loaded correctly or key is missing
    print("Warning: SUBWAY_API_KEY not found in environment, checking direct variable...")
    # This script is meant to be run after .env is created
    pass

BASE_URL = "http://swopenapi.seoul.go.kr/api/subway"

def test_api():
    line_name = "1호선"
    url = f"{BASE_URL}/{API_KEY}/json/realtimePosition/0/5/{line_name}"
    print(f"Testing URL: {url.replace(API_KEY, '***KEY***')}") # Hide key in logs
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if "server_error" in data:
             print("Server Error reported in JSON.")
             return

        if "realtimePositionList" in data:
            count = len(data["realtimePositionList"])
            print(f"SUCCESS: Retrieved {count} trains for {line_name}.")
            # Print first train for verification
            first = data["realtimePositionList"][0]
            print(f"Sample Train: {first['trainNo']} - {first['statnNm']} ({first['trainSttus']})")
        else:
            print("Response received but no 'realtimePositionList'. details:")
            print(json.dumps(data, indent=2, ensure_ascii=False))
            
    except Exception as e:
        print(f"FAILED: {e}")

if __name__ == "__main__":
    if not API_KEY:
        print("Error: SUBWAY_API_KEY is not set.")
    else:
        test_api()
