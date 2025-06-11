# CycleSense

CycleSense is a command-line based menstrual cycle tracking tool designed for individuals who want to monitor their health patterns, predict future cycles, and visualize trends over time.

## 🔍 Features

- Track new cycle entries with:
  - Last period date
  - Cycle length (in days)
  - Symptoms (optional)
  - Health goals (optional)
-  Generate cycle history chart using Matplotlib
-  Predict:
  - Next period date
  - Ovulation window
  - Fertile window
  - PMS start date
-  Stores all entries in:
  - `cycles.csv` (for cumulative history)
  - Timestamped `.json` files (for backups)

## 💻 Technologies Used

- **Python 3**
- `pandas` — for CSV storage and processing
- `matplotlib` — for plotting graphs
- `datetime` — for accurate predictions
- `json` — for backup snapshots

## 🧪 How to Run

```bash
git clone https://github.com/Yash19242/CycleSense
cd CycleSense
python main.py
```

## 📂 Project Structure

```
CycleSense/
├── main.py               # CLI entry point
├── tracker.py            # Cycle prediction + logic
├── plotter.py            # Graph generator using matplotlib
├── data/
│   ├── cycles.csv        # Saved data
│   └── *.json            # Backups for each entry
└── README.md             # Project documentation
```

## 📌 Example Usage

```bash
=== CycleSense – Menstrual Health Tracker ===

1. Track new cycle
2. View cycle history chart
Choose an option: 1

Name: Anjali
Last Period Date (YYYY-MM-DD): 2025-06-01
Cycle Length (days): 28
Symptoms: cramps, mood swings
Goal: stay hydrated
```

## 🚀 Future Plans

- Add irregularity detection using standard deviation
- Integrate AI assistant for symptom analysis and advice
- Export PDF summaries

## 🤝 Contributions

This project is solo-built as part of a portfolio for Python and data science internships.

Feel free to fork, contribute, or reach out on LinkedIn:
[linkedin.com/in/yash-sheth-83710136a](https://www.linkedin.com/in/yash-sheth-83710136a)
