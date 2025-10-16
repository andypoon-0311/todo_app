# To do list 2

#array where task is stored
tasks = []

#shows list of task
def listTasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks):
            print(f"{i}. {task}")
           
#Adds task to array
def addTask():
    task = input("Enter task: ")
    tasks.append(task)
    print("Your task is added")

#removes task array
def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Choose the # of the task you want to delete: "))
        if 0 <= taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task #{taskToDelete} has been deleted.")

        else:
            print(f"Task #{taskToDelete} was not found.")
            

    except:
        print("Invalid input. ")
num = 0

#main function
print("Welcome to you to do list!")
lineZero = "To do list"
tasks.append(lineZero)
while num == 0: #while shows edit list, view list, leave
    print("\n")
    print("What do you want to to your list? Select a number")
    print("1.Edit list")
    print("2. View all task")
    print("3. Leave")
    choice1 = input("Enter choice here: ")

    if choice1 == "1": #Edit page dashboard
        num1 = 0
        while num1 == 0: #while shows add task, delete task, leave
            print("\n")
            print("Select what your changing to you list")
            print("1. Add Task")
            print("2. Delete task")
            print("3. Go back to home page")
            choice2 = input("Enter choice here: ")

            if choice2 == "1":
                #addTask() funtion
                print("\n")
                addTask()
                
            elif choice2 == "2":
                #deleteTask function
                print("\n")
                deleteTask()

            elif choice2 == "3":  #break out of while
                num1 = num1 + 1;

            else:
                print("Invalid answer, please re-enter")

    elif choice1 == "2": #View List dashboard
        print("\n")
        #print array list
        listTasks()
        

    elif choice1 == "3": #break out of while to go home
        num = num + 1;
    else:
        print("Invalid answer, please re-enter")
print("Good bye")

    
