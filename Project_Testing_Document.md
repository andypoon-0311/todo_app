# Project Testing Document

## 1. Introduction and Scope
Project Overview: Our goal of our project is to for the user to be able to create and add task to a to list. Users can mark task as complete and remove them.

Test Objectives: During testing, we are trying to find any program bugs or errors that need to be fixed. We are going to make sure all methods work as intendented. When users adds tasks, the to do list should show them as the order they were put in. When a user selects to remove a task from the list, the task should not appear in the list once the command is done. If the user wants to mark the task as complete, a mark should show up next to that task. If all of the methods work, the software is good enough to realease. 

In-Scope/Out-of-Scope: In our first round of testing, we will test if a task can be properly added to the to do list and if it can be marked as complete. Removing a task testing will be apart of the next plan. 

## 2. Functional Testing Strategy (Levels)
Unit Testing: First, we are going to run all of the programs code at once to see what units need work on. Them We are breaking up the code test into seperate test depending on the type of the method the code corresponds with. We will descide what other test to run as we right the code.

Feature Testing: We are going to make sure that all of the functions meet the users needs. Weather they want to add or remove task from there list. We will test this by see if a task is added to a list, that data is put into the JSON file. If a task is being romoved from the list, it should be removed from the JSON File. 

System Testing (End-to-End): Our goal is to make sure the software works as intended. If data is properly being added or removed from the JSON File. We will go back and correct the errors until it is correct.



## 3. Testing Types and Goal
User Testing: We wanted to show how this software can usful to users since itis and electronic to do list. Today many people to their work from computers or other smart gagets. This appilcation will keep a user course on a do list and their other work all in on spot. Their to do list should be easy to find on their computer and can run when other applications are running.  

User Testing: We are going to select a group of about a dozen users. These users will use the todo application to assist in their day to day tasks. We plan on selecting users in mulitple industries as one of the goals of the application is to be general purpose for any use case. The result we are hoping for is that users find the application simple and easy to use. It should improve a users work flow.

Performance and Load Testing: The achieve this testing case, because the application does not have an API we are going to manaully stress the application by continuously adding tasks. If that succeeds without crashing the application, we will proceed with continuously deleting tasks. The expected result is that the application should remain stable. Another test that we would like to do have an absurdly large input to test for stability and security considerations such as a buffer overflow.

Security Testing: Currently user data is stored in a local json file. The data within the json file is in plaintext. If users input sensitive information into the json file, there is no authentication mechanism or encryption. Unauthorized access to the json file would constitute a violation of confidentiality from the CIA triad. It is also planned to scan the source code and application with a vulnerability scanner like Nessus. Testing for buffer overflow will also be conducted to mitigate any unexpected behavior if buffer overflow is present.

## 4. Test Design Approach

There are only 3 input fields allowed by the application. Task Title, Description of Task, and Due Date. Input should all be treated as a string. A user should not be able to execute python code within these input fields. A user should also be unable to execute shell code, and or powershell or bash within these input fields. We will attempt to use scripting languages and python within the input fields to see if we can achieve arbitrary execution of the respective language. We will also test various lengths of input strings to ensure code stability. We will also test null inputs within the title field as this is the only required input field.

## 5. Test Enviroment and Delieverables

Test Environment: The application is meant to be cross platform for Windows, MacOS, and Linux. Due to this requirement, we will require three devices with its respective operating system. We may also choose to spin up virtual machines instead if it is not feasible to obtain three workstations. Due to Linux having dozens of flavors, it may be wise to go with the virtual machine approach. For Linux, we will test with the most popular distributions (Ubuntu, Arch, Debian, Fedora). We will also test with multiple desktop environments (GNOME, KDE, MATE) and desktopless environments (Hyprland, I3, DWM) to ensure stability and functionality on Linux.

Test Deliverables: Testing will be conducted on each input field. Each input field will be tested with multiple variations of string values. Some of these string values will be large, and we will also test null inputs. Screenshots will be taken of each test case to be compiled into a final test summary report. As mentioned above part of the test cases will be inputing values that may be potentially intepretted as executable code. Screenshots will be taken here as well. 