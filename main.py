# main.py
# Entry point of CycleSense – handles user input and main menu

from tracker import predict_cycle
from plotter import plot_cycle_history

def main():
    print("=== CycleSense – Menstrual Health Tracker ===\n")

    print("1. Track new cycle")
    print("2. View cycle history chart")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        last_period = input("Enter the last period date (YYYY-MM-DD): ")
        cycle_length = int(input("Enter your average cycle length in days: "))
        
        # Ask for optional details
        symptoms = input("Enter any symptoms (comma-separated): ")
        goal = input("Enter a goal for this cycle (optional): ")

        # Run prediction and save
        predict_cycle(name, age, last_period, cycle_length, symptoms, goal)

    elif choice == "2":
        plot_cycle_history()

    else:
        print("Invalid option. Please run again and choose 1 or 2.")

if __name__ == "__main__":
    main()
