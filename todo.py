FILENAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILENAME) as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def save_tasks():
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

tasks = load_tasks()

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def delete_task():
    show_tasks()
    try:
        number = int(input("Task number to delete: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks()
            print(f"Deleted: {removed}")
        else:
            print("Number out of range.")
    except ValueError:
        print("Please enter a number.")

def main():
    while True:
        print("\n1. Add task\n2. View tasks\n3. Delete task\n4. Quit")
        choice = input("Choose: ")
        if choice == "1":
            task = input("Task: ").strip()
            if task:
                tasks.append(task)
                save_tasks()
            else:
                print("Task cannot be empty.")
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()