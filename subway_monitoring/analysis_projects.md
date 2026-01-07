# Data Analysis Projects for Subway Operations Monitoring

These projects use `realtime_subway_positions` to monitor operational efficiency and identify issues.

## 1. Train Headway Consistency Monitor
**Goal:** Detect irregular intervals (bunching or gapping) between trains to ensure consistent service.

*   **Logic:**
    1.  Filter for `train_status_code = 1` (Arrival at station).
    2.  Group by `station_id` and `direction_type`.
    3.  Sort by `last_received_time`.
    4.  Calculate `delta_t` = Time(Train_B) - Time(Train_A).
*   **Metrics:**
    *   **Headway Variance:** High variance suggests irregular service.
    *   **Gap Alerts:** If `delta_t` > threshold (e.g., 10 mins during peak), flag as "Gap".
    *   **Bunching Alerts:** If `delta_t` < threshold (e.g., 2 mins), flag as "Bunching".

## 2. Station Dwell Time Analysis
**Goal:** Identify stations where trains stay longer than expected, causing potential delays.

*   **Logic:**
    1.  Identify a single station visit for a specific `train_number`.
    2.  Find the timestamp for `train_status_code = 1` (Arrive).
    3.  Find the timestamp for `train_status_code = 2` (Depart) for the *same* trains at the *same* station.
    4.  Calculate `dwell_time` = Time(Depart) - Time(Arrive).
*   **Metrics:**
    *   **Average Dwell Time per Station:** Compare against network average.
    *   **Dwell Time Anomalies:** Identify specific stations or times of day with excessive dwell times.

## 3. Real-time Congestion/Bottleneck Heatmap
**Goal:** Visualize train density to spot network bottlenecks in real-time.

*   **Logic:**
    1.  Define a time window (e.g., last 5 minutes).
    2.  Count unique `train_number` entries visible in the system within that window, grouped by `line_id` and potentially mapped to segments (Station A -> Station B).
*   **Metrics:**
    *   **Trains per Line:** total active trains.
    *   **Segment Density:** High density in a short segment indicates a bottleneck (traffic jam).
