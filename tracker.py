# tracker.py
# Contains logic to predict cycle, calculate dates, track symptoms,
# save data to CSV and JSON, and detect irregular patterns.

from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import os
import json

def predict_cycle(name, age, last_period_str, cycle_length, symptoms, goal):
    try:
        # Convert user-entered date string to a datetime object
        last_period = datetime.strptime(last_period_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    # Predict important dates
    next_period = last_period + timedelta(days=cycle_length)
    ovulation = last_period + timedelta(days=cycle_length // 2)
    fertile_start = ovulation - timedelta(days=2)
    fertile_end = ovulation + timedelta(days=2)
    pms_start = next_period - timedelta(days=5)

    # Print predictions
    print("\nSummary:")
    print("User:", name)
    print("Age:", age)
    print("Last Period:", last_period.date())
    print("Next Period Expected:", next_period.date())
    print("Fertile Window:", fertile_start.date(), "to", fertile_end.date())
    print("Ovulation Day:", ovulation.date())
    print("PMS Likely Starting:", pms_start.date())

    if symptoms.strip():
        print("Symptoms:", symptoms)
    if goal.strip():
        print("Goal for this cycle:", goal)

    # Save to CSV and JSON
    save_data(name, age, last_period.date(), cycle_length, next_period.date(),
              ovulation.date(), fertile_start.date(), fertile_end.date(),
              pms_start.date(), symptoms, goal)
    
    # Check irregularity
    check_irregularity()


def save_data(name, age, last_period, cycle_length, next_period, ovulation,
              fertile_start, fertile_end, pms_start, symptoms, goal):
    file_path = "data/cycles.csv"
    new_entry = {
        "Name": name,
        "Age": age,
        "Last Period": last_period,
        "Cycle Length": cycle_length,
        "Next Period": next_period,
        "Ovulation": ovulation,
        "Fertile Start": fertile_start,
        "Fertile End": fertile_end,
        "PMS Start": pms_start,
        "Symptoms": symptoms,
        "Goal": goal
    }

    # Convert to DataFrame to store in CSV
    df = pd.DataFrame([new_entry])

    if os.path.exists(file_path):
        # Append to existing CSV without headers
        df.to_csv(file_path, mode='a', index=False, header=False)
    else:
        # Create new CSV with headers
        df.to_csv(file_path, index=False)

    # Save JSON backup
    json_filename = f"data/backup_{last_period}.json"
    with open(json_filename, "w") as f:
        json.dump(new_entry, f, indent=2, default=str)

    print("Data saved to CSV and JSON.")


def check_irregularity():
    file_path = "data/cycles.csv"
    if not os.path.exists(file_path):
        return

    df = pd.read_csv(file_path)
    
    if len(df) < 3:
        return  # Need at least 3 cycles to check trend

    # Calculate standard deviation
    std_dev = np.std(df["Cycle Length"])

    if std_dev > 3:
        print("Warning: Your cycles seem irregular (std deviation =", round(std_dev, 2), ")")
    else:
        print("Your cycle length is consistent.")