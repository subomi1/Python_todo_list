import json
import os
File_Name = "tasks.json"
def load_tasks():
    if not os.path.exists(File_Name):
        return[]
    with open(File_Name, "r") as file:
        return json.load(file)
    
    
def save_tasks(tasks):
    with open(File_Name, "w") as file:
        json.dump(tasks, file, indent=4)
        

def show_tasks(tasks):
    if not tasks:
        print("No tasks found")
        return
    for index, task in tasks:
        status = "✅" if task["done"] else "❌"
        print(f"{index + 1}. {task["title"]} - {status}")
        
    
    
        
    
def main():
    tasks = load_tasks()
    while True:
        print("📑 To-Do List")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Mark a task as done")
        print("4. Quit")
        option = int(input("Choose an option from(1-4): "))
    if option == 1:
        show_tasks(tasks)
    elif option == 2:
        title = input("Enter task ")