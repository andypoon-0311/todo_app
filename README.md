# Overview
This application is a simple and easy to use to do list. It will store data written to it on a JSON file stored locally on the device. Data is stored locally only so it is the user's responsibility to back up the data.

The primary goal of this application is to store tasks, as a reminder, as an organizer, or whatever else you choose to use its features. The ui files are included in this repository as it is essential for the application, that being said if the look and feel does not suit your needs it is easily modifiable, or users may also choose to use qt designer (installed with pyside6) to generate new ui files. Another concern of ours was privacy. Applications and many Saas solutions provides a lot of convenience through redundancy and availability. However, for the more privacy concious users, this application will not store your data anywhere besides the local **toDoList.json** file. This way privacy level is decided by the end user. You may store this file in one drive, iCloud, or any other cloud storage solution if you wish. Please note that by doing so modifications may have to be made to the **toDoList.py** file so that the current path is established for the filename variable.

The application will be written in python on the Qt SDK (pyside6). The application must be cross platform compatiable for Windows, MacOS, and Linux hence Qt.

A compiled executable may be made by using PyInstaller to compile the source code. There is already a compiled version of this in dist/main but it is only compatiable with linux. If you wish to use a compiled version please install pyinstaller. Users may also choose to clone the repository, install all dependencies and run it just as a .py. Dependencies are located in requirements.txt.

## User Stories and Scenarios
. A user has trouble remembering what chores they have to do. They want to use this software to create a to-do list.

. Throughout the day the user remembers more tasks they have to do. They are able to add more tasks to their list.

. Once a task is complete, they are able to remove it from their list.

. If the user wants to see all the task they have, they are able to view their list

. When the user is done editing their list, they are able to quit the software. 


## Use Case Diagrams 

| Feature | Focus | Symbol |
|---------|-------|--------|
| Actor   | This application is meant for general purpose usage, anyone may use it | Stick Figure |
| Use Case| Organize tasks into one application without having to pay for a subscription and all your data stays local | Oval |
| System Boundary | To maintain privacy all data is local to the end user. The only external entity that interacts with the application is therefore the end user | Rectangle | 

## Adding Task 

| Feature | Focus | Symbol |
|---------|-------|--------|
| Actor   | User | Stick Figure |
| Use Case| User wants to add task to list | Oval |
| Flow| User selects that they want to edit their list. They select add task. They input their task and gets saved to a JSON file. When they complete the task, they are able to mark it as complete. |


### Diagram

<p align="center">
    <img src="Documents/todoApp_use_case_diagram.png" alt="Use Case Diagram" width="600">
</p>

## Deleting Task 

| Feature | Focus | Symbol |
|---------|-------|--------|
| Actor   | User | Stick Figure |
| Use Case| User wants to remove task to list | Oval |
| Flow| Once user completes a task, they have option to remove it. When the deleteTask method is called. The selected task is removed from list. |

### Diagram
<p align="center">
    <img src="Documents/IMG_0686.png" alt="Use Case Diagram" width="600">
</p>

Every action taken is by the end user. There are no further external entities. An end user should be able to add a task, complete a task, and view all of their tasks. 

## System Architecture

<p align="center">
    <img src="Documents/system_architecture.png" alt="System Architecture" width="600">
</p>

There are purposely minimal system components, as you can see from the diagram above. The application is meant to be simple and light weight as to not introduce much complexity to adding a task to your todo list. It is also minimal by design so that end users may customize the look and feel to suit their requirements. And to reiterate, the data is stored locally in plaintext in *toDoList.json*, it is therefore the responsiblity of the end user to maintain the integrity and redundancy of their data within the application. If cloud components, such as cloud storage was added, there would be no way with certainty that an end user can guarantee the privacy of their data. As who's to say that no one is looking at your data when it is stored external to your device by a 3rd party to include the developers of this application.

The user interface is supported by the Qt SDK for python. The .ui files were exported from the Qt designer.

## User Interface Design

## Home Page 
Users will see on option to edit their list. They can either add a task or remove task
<p align="center">
    <img src="Documents/Home Page.png" alt="Use Case Diagram" width="400">
</p>

## Add Task Page
Users will have a place to type in the task they want to add to their list. Their input will be added to the JSON File
<p align="center">
    <img src="Documents/Add Task Page.png" alt="Use Case Diagram" width="400">
</p>

## Mark as complete
The user will see their whole list of task. They get to select the one they want to mark as complete.
<p align="center">
    <img src="Documents/Complete.png" alt="Use Case Diagram" width="400">
</p>

## Delete Task Page
Users will have a place to type which task they want to remove from their list. The task will be removed from the JSON File.
<p align="center">
    <img src="Documents/Delete Task Page.png" alt="Use Case Diagram" width="400">
</p>

<p align="center">
    <img src="Documents/Deleted Task.png" alt="Use Case Diagram" width="400">
</p>




## Detail Designs
### toDoList.py

**save_tasks** : It's sole purpose is to write data to the json file.

**load_tasks** : This function passes the json structure to *main.py* to display the list of tasks. If the *toDoList.json* is empty:

```json
{
    "tasks" : []
}
```
It will return an empty array and MainWindow will display "No tasks yet".

**add_task** : This function adds a task to the json file. It's structure is as follows:

```json
{
    "title": title,
    "task": task,
    "due_date": due_date,
    "created_date": now
}
```

**deleteTask** : Removes a task from the json file once marked complete by the complete button on the MainWindow. It first calls **load_tasks** and sets the found variable to false. It proceeds to iterate through the json structure to find the corresponding title value. Once the task is found, found inherits the value of true and returns found. If found remains false the application will state that the task was not found. Though this should never happen as the application should refresh after each action.

### main.py

#### AddTaskDiaglog

**__init__(self)** : This defines the constructor for the add task "pop up". It is a dialog box in Qt terms. It starts by calling the parent from the Qt SDK **QDialog.__init__()** ensuring that everything is initialized properly. We use QFile here because it is Qt's way of file handling, and we open the ui file in read only mode because no write operations will occur to the ui file as it would render it instable. We proceed to load the gui_file (add_task.ui) and this is embeded within the QDialog making it a child of QDialog. The button accepts two "signals" so to speak. It can either reject the changes where no write action would occur or it can accept the changes where the changes would be written to the json file and rendered in the MainWindow.

**get_task_data** : "titleInput", "descInput", and "dueInput" finds the Qt input widgets by their object names. Please note that if modifications are made to the ui file, the object name must remain the same if no changes are to be made to the python code. Then it proceeds to extract the contents from the input fields to be displayed in the MainWindow, stripping all leading and trailing whitespace.

#### MainWindow

**__init__(self)** : This function initializes the main window. Loading "mainWindow.ui". Note we did not use "super()" here, it was not working most likely due to a flaw in the logic, but this has been mitigated with the **show** function. Again we open the ui file in read only mode. Because we didn't use super() here we couldn't do this like in **AddTaskDialog**:

```python
self.window.setParent(self)
```

Instead we had to set self.window to refer to the gui window:

```python
self.window = loader.load(ui_file)
```

Next we proceed to insert all of the task widgets in a vertical layout. Meaning the tasks will be displayed in a vertical fashion (top to bottom). Note the "scrollAreaWidgetContents" will not appear until there are enough tasks to fill the vertical layout window. The button widget in this main window is to add a task. Once it is clicked it will populate the AddTaskDialog window, and once that action is completely the MainWindow will refresh immediately.

**refresh_tasks** : This starts by getting a count of tasks currently in the layout. We refresh by removing all the widgets in the MainWindow vertical layout until there are no widgets left, then we load the tasks again from the json file. If there are no task the vertical layout will simply state "No tasks yet". The for loop here just iterates through the json structure looking for existing task and repopulates its widget in the vertical layout.

**open_add_tasks** : As you can guess is used to open the add task window. Notice in **__init__**:

```python
self.add_button.clicked.connect(self.open_add_task)
```

Here we check to ensure the user entered at least a value for the title, else we will use Qt to throw an error stating that a "Title is Required". If the task was successfully added then we proceed to refresh the MainWindow with the addition of the newly added task.

**complete_task** : Calls the *deleteTask* function passing the title of the completed task. This task will be removed from the json structure and the MainWindow will refresh with the subtraction of the completed task.

The main function starts with the common:

```python
if __name__ == "__main__"
```

Instructing python to only execute this file if it is being called directly. This lets python know this is the main file. The app variable creates the Qt application object so to speak.

```python
app = QApplication([])
app.exec()
```

The ui variable just renders the MainWindow upon start up of the applciation. Without it the app would run but nothing would be rendered.

```python
ui = MainWindow()
ui.show()
```

## Project Testing Document

## 1. Introduction and Scope
Project Overview: Our goal of our project is to for the user to be able to create and add task to a to list. Users can mark task as complete and remove them. This software should help users keep track of what they have to do throughout the day. 

Test Objectives: During testing, we are trying to find any program bugs or errors that need to be fixed. We are going to make sure all methods work as intended. When users adds tasks, the to do list should show them as the order they were put in. When a user selects to remove a task from the list, the task should not appear in the list once the command is done. If the user wants to mark the task as complete, a mark should show up next to that task. If all of the methods work, the software is ready to realease. 

In-Scope/Out-of-Scope: In our first round of testing, we will test if a task can be properly added to the to do list and if it can be marked as complete. Removing a task testing will be apart of the next plan. 

## 2. Functional Testing Strategy (Levels)
Unit Testing: First, we will descide which specific test to run as we right the code. We will test every possible senario and make sure the program works as intended. The first test we will do is run all part of the program at once. This will show us what functions have errors and need need to be worked on. Then we are testing the code in smaller amounts. The amounts depend on the type of code  and if it corresponds to a certain function. 

Feature Testing: We are going to make sure that all of the functions meet the users needs. Weather they want to add or remove task from there list. We will test this by seeing if a task is added to a list is stored into a JSON file. If a task is being deleted from the list, the data should be removed from the JSON File. 

System Testing (End-to-End): Our goal is to make sure the software works as intended. The data should proply be added or removed from the JSON File. For example if a user adds a task to their list and it is not saving in the JSON file We will go back and correct the errors until the software works.


## 3. Testing Types and Goal
User Testing: We are going to select a group of about a dozen users. These users will use the todo application to assist in their day to day tasks. We plan on selecting users in mulitple industries as one of the goals of the application is to be general purpose for any use case. The result we are hoping for is that users find the application simple and easy to use. It should improve a users work flow.

Performance and Load Testing: To achieve this testing case, because the application does not have an API we are going to manaully stress the application by continuously adding tasks. If that succeeds without crashing the application, we will proceed with continuously deleting tasks. The expected result is that the application should remain stable. Another test that we would like to do have an absurdly large input to test for stability and security considerations such as a buffer overflow.

Security Testing: Currently user data is stored in a local json file. The data within the json file is in plaintext. If users input sensitive information into the json file, there is no authentication mechanism or encryption. Unauthorized access to the json file would constitute a violation of confidentiality from the CIA triad. It is also planned to scan the source code and application with a vulnerability scanner like Nessus. Testing for buffer overflow will also be conducted to mitigate any unexpected behavior if buffer overflow is present.

## 4. Test Design Approach

There are only 3 input fields allowed by the application. Task Title, Description of Task, and Due Date. Input should all be treated as a string. A user should not be able to execute python code within these input fields. A user should also be unable to execute shell code, and or powershell or bash within these input fields. We will attempt to use scripting languages and python within the input fields to see if we can achieve arbitrary execution of the respective language. We will also test various lengths of input strings to ensure code stability. We will also test null inputs within the title field as this is the only required input field.

## 5. Test Enviroment and Delieverables

Test Environment: The application is meant to be cross platform for Windows, MacOS, and Linux. Due to this requirement, we will require three devices with its respective operating system. We may also choose to spin up virtual machines instead if it is not feasible to obtain three workstations. Due to Linux having dozens of flavors, it may be wise to go with the virtual machine approach. For Linux, we will test with the most popular distributions (Ubuntu, Arch, Debian, Fedora). We will also test with multiple desktop environments (GNOME, KDE, MATE) and desktopless environments (Hyprland, I3, DWM) to ensure stability and functionality on Linux.

Test Deliverables: Testing will be conducted on each input field. Each input field will be tested with multiple variations of string values. Some of these string values will be large, and we will also test null inputs. Screenshots will be taken of each test case to be compiled into a final test summary report. As mentioned above part of the test cases will be inputing values that may be potentially intepretted as executable code. Screenshots will be taken here as well. 

