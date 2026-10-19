tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def main():
    while True:
        print("\n1. Add task\n2. View tasks\n3. Quit")
        choice = input("Choose: ")
        if choice == "1":
            tasks.append(input("Task: "))
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()