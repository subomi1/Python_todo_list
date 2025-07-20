import json
import os
File_Name = "tasks.json"


def load_tasks():
    if not os.path.exists(File_Name):
        return []
    with open(File_Name, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(File_Name, "w") as file:
        json.dump(tasks, file, indent=4)


def show_tasks(tasks):
    if not tasks:
        print("No tasks found")
        return
    for index, task in enumerate(tasks):
        status = "✅" if task['done'] else "❌"
        print(f"{index + 1}. {task["title"]} - {status}")


def main():
    tasks = load_tasks()
    while True:
        print("📑 To-Do List")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Mark a task as done")
        print("4. Delete  a task")
        print("5. Edit a task title")
        print("6. Clear all tasks")
        print("7. Quit")
        option = int(input("Choose an option from(1-6): "))
        if option == 1:
            show_tasks(tasks)
        elif option == 2:
            title = input("Enter task title: ")
            tasks.append({"title": title, "done": False})
            save_tasks(tasks)
            print("Task added")
        elif option == 3:
            show_tasks(tasks)
            index = int(
                input("Enter the task number to mark as complete: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index]["done"] = True
                save_tasks(tasks)
                print("Task marked as complete.")
            else:
                print("invalid task number.")
        elif option == 4:
            show_tasks(tasks)
            try: 
                index = int(input("Enter the task number you want to delete: ")) - 1
                if 0 <= index < len(tasks):
                    delete = tasks.pop(index)
                    save_tasks(tasks)
                    print(f"Deleted task: {delete['title']}")
                else:
                    print("Invalid task number")
            except ValueError:
                print("please enter a valid number")
        elif option == 5:
            show_tasks(tasks)
            try:
                index = int(input("Enter the number of the task in which the title you want to change: ")) - 1
                if 0 <= index < len(tasks):
                    title_change = input("Enter the name in which you want to change it to: ").strip()
                    tasks[index]["title"] = title_change
                    save_tasks(tasks)
                    print(f"Task {index + 1} title updated to: {title_change}")
                else:
                    print("Invalid task number")
            except ValueError:
                print("please enter a valid number")
        elif option == 6:
            show_tasks(tasks)
            answer1 = input("Are you sure you want to clear all tasks (Y)es or (N)o: ").lower()
            if answer1 == "y":
                tasks.clear()
                save_tasks(tasks)
                print("All tasks cleared")
            elif answer1 == "n":
                print("No tasks were cleared")
            else:
                print("Invalid input")
        elif option == 7:
            print("Goodbye")
            break
        else:
            print("invalid choice. Please enter 1, 2, 3 or 4.")


main()
