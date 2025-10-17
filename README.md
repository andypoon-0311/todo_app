# Overview
This application is a simple and easy to use to do list. It will store data written to it on a JSON file stored locally on the device. Data is stored locally only so it is the user's responsibility to back up the data.

The primary goal of this application is to store tasks, as a reminder, as an organizer, or whatever else you choose to use its features. The ui files are included in this repository as it is essential for the application, that being said if the look and feel does not suit your needs it is easily modifiable, or users may also choose to use qt designer (installed with pyside6) to generate new ui files.

The application will be written in python on the Qt SDK (pyside6). The application must be cross platform compatiable for Windows, MacOS, and Linux hence Qt.

A compiled executable may be made by using PyInstaller to compile the source code. There is already a compiled version of this in dist/main but it is only compatiable with linux. If you wish to use a compiled version please install pyinstaller. Users may also choose to clone the repository, install all dependencies and run it just as a .py. Dependencies are located in requirements.txt.

## Use Case

| Feature | Focus | Symbol |
|---------|-------|--------|
| Actor   | This application is meant for general purpose usage, anyone may use it | Stick Figure |
| Use Case| Organize tasks into one application without having to pay for a subscription and all your data stays local | Oval |
| System Boundary | To maintain privacy all data is local to the end user. The only external entity that interacts with the application is therefore the end user | Rectangle | 

### Diagram

<p align="center">
    <img src="Documents/todoApp_use_case_diagram.png" alt="Use Case Diagram" width="600">
</p>

## System Architecture

<p align="center">
    <img src="Documents/system_architecture.png" alt="System Architecture" width="600">
</p>