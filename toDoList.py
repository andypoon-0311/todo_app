# To do list 2
import json
import os
from datetime import datetime
from PySide6 import QtCore, QtWidgets, QtGui
# CReate JSON Structure
filename = "toDoList.json"

# save tasks to json file for persistence
def save_tasks(tasks):
    with open (filename, "w") as f:
        json.dump({"tasks": tasks}, f, indent=4)

#loads task
def load_tasks():
    if not os.path.exists(filename):
        save_tasks([]) #Returns empty list and creates file if file path does not exist
        return []
    with open(filename, "r") as f:
        return json.load(f).get("tasks", [])

tasks = load_tasks()

#Adds task to array
def add_task(title, task, due_date):
    tasks = load_tasks()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tasks.append({
        "title": title,
        "task": task,
        "due_date": due_date,
        "created_date": now
    })
    save_tasks(tasks)
    print("Your task is added")

#removes task array
def deleteTask(taskToDelete):
    tasks = load_tasks()
    found = False

    for i, task in enumerate(tasks):
        if task["title"].lower() == taskToDelete.lower():
            tasks.pop(i)
            save_tasks(tasks)
            found = True
            print(f"[+] Task #{taskToDelete} has been deleted")
            return found
    if found == False:
        print(f"[-] Task #{taskToDelete} was not found")
        return found

#main function
#print("Welcome to you to do list!")
#lineZero = "To do list"
#tasks.append(lineZero)
#while num == 0: #while shows edit list, view list, leave
#    print("\n")
#    print("What do you want to to your list? Select a number")
#    print("1.Edit list")
#    print("2. View all task")
#    print("3. Leave")
#    choice1 = input("Enter choice here: ")

#    if choice1 == "1": #Edit page dashboard
#        num1 = 0
#        while num1 == 0: #while shows add task, delete task, leave
#            print("\n")
#            print("Select what your changing to you list")
#            print("1. Add Task")
#            print("2. Delete task")
#            print("3. Go back to home page")
#            choice2 = input("Enter choice here: ")

#            if choice2 == "1":
                #addTask() funtion
#                print("\n")
#                addTask()
                
#            elif choice2 == "2":
                #deleteTask function
#                print("\n")
#                deleteTask()

 #           elif choice2 == "3":  #break out of while
 #               num1 = num1 + 1;

#            else:
#                print("Invalid answer, please re-enter")

#    elif choice1 == "2": #View List dashboard
#        print("\n")
        #print array list
#        listTasks()
        

#    elif choice1 == "3": #break out of while to go home
#        num = num + 1;
#    else:
#        print("Invalid answer, please re-enter")
#print("Good bye")

    
