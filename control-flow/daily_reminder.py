
def main():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task"
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task"
        case "low":
            reminder = f"Note: '{task}' is a low priority task"
        case _:
            reminder = f"Task priority '{priority}' not recognized."

    if time_bound == "yes" and priority in ["high", "medium"]:
        reminder += " that requires immediate attention today!"
    elif time_bound == "no" and priority in ["high", "medium"]:
        reminder += ". Please complete it as soon as possible."
    elif time_bound == "no" and priority == "low":
        reminder += ". Consider completing it when you have free time."

    print(reminder)

if __name__ == "__main__":
    main()
