# plotter.py
# Contains graphing logic to visualize cycle history using matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_cycle_history():
    path = "data/cycles.csv"

    # Check if file exists
    if not os.path.exists(path):
        print("No cycle history found.")
        return

    # Read the CSV data
    df = pd.read_csv(path)

    # Convert "Last Period" column to datetime for sorting
    df["Last Period"] = pd.to_datetime(df["Last Period"])
    df = df.sort_values(by="Last Period")

    # Plot cycle lengths over time
    plt.figure(figsize=(10, 5))
    plt.plot(df["Last Period"], df["Cycle Length"], marker='o', linestyle='-', color='teal', label="Cycle Length")

    plt.title("Menstrual Cycle Length Over Time")
    plt.xlabel("Last Period Date")
    plt.ylabel("Cycle Length (days)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
