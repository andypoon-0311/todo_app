# gui for toDoList.py
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox, QDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import toDoList

# Implementing add task as a separate pop up window
class AddTaskDialog(QDialog):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        gui_file = QFile("add_task.ui")
        gui_file.open(QFile.ReadOnly)
        self.window = loader.load(gui_file)   # this is the pop up window for adding a task
        gui_file.close()
        #self.window.setParent(self)

        task_layout = QVBoxLayout(self)
        task_layout.addWidget(self.window)
        self.setLayout(task_layout)

        buttonBox = self.window.findChild(QWidget, "buttonBox")
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
    
    def get_task_data(self):
        titleInput = self.window.findChild(QWidget, "TitleInput")
        descInput = self.window.findChild(QWidget, "descriptionInput")
        dueInput = self.window.findChild(QWidget, "dueDateInput")

        title = titleInput.text().strip()                                                       # Strip is to remove the whitespace if there are any in user input. Ex: "  my example" becomes "my example"
        descrip = descInput.toPlainText().strip()
        due = dueInput.text().strip()
        return title, descrip, due

# this is main window where all tasks stored in toDolist.json will be stored at
class MainWindow:
    def __init__(self):
        loader = QUiLoader()
        ui_file = QFile("mainWindow.ui")
        ui_file.open(QFile.ReadOnly)
        self.window = loader.load(ui_file) # Takes the mainWindow.ui file to load the gui
        ui_file.close()

        self.scroll_content = self.window.findChild(QWidget, "scrollAreaWidgetContents")        #Getting the scroll widget from ui file
        self.add_button = self.window.findChild(QPushButton, "addTaskButton")                   #Getting the addTaskButton widget from the ui file

        #Main window should have a vertical layout from the ui file
        #This window will display tasks that are stored in the toDoList.json file
        self.task_layout = QVBoxLayout(self.scroll_content)
        self.scroll_content.setLayout(self.task_layout)

        self.add_button.clicked.connect(self.open_add_task)                                     #Opens the add task window (pop up) when clicking the add task button
        self.refresh_tasks()                                                               

    def show(self):
        self.window.show()                                                                      #Couldn't figure out why the normal super().__init__() method was not working; this is a work around                                             

    def refresh_tasks(self):
        while self.task_layout.count():
            item = self.task_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        tasks = toDoList.load_tasks()
        if not tasks:
            self.task_layout.addWidget(QLabel("No tasks yet."))
            return

        for task in tasks:
            title = task.get("title", "Untitled")
            due = task.get("due_date", "No due date")
            descrip = task.get("task", "")
            container = QWidget()
            layout = QVBoxLayout(container)
            titleBox = QLabel(f"{title} | Due : {due}")
            descriptionBox = QLabel(descrip)
            ok_button = QPushButton("Complete")
            ok_button.clicked.connect(lambda _, x=title: self.complete_task(x))             #Qt uses signals; in this case we are looking for the clicked signal; connects to complete task and x obviously is equal to the current title that was marked as complete
            layout.addWidget(titleBox)
            layout.addWidget(descriptionBox)
            layout.addWidget(ok_button)
            self.task_layout.addWidget(container)
        self.task_layout.addStretch()                                                       #Lets us add tasks to the top of the layout leaving space at the bottom for a quote on quote stretch (white space)

    def open_add_task(self):
        dialog = AddTaskDialog()                                                            #Used dialougue box widget in Qt Designer for adding task
        if dialog.exec():
            title, descrip, due = dialog.get_task_data()
            if not title:
                QMessageBox.warning(self.window, "Error", "[-] Title Is Required")          #Forces the user to at least input a title, everything else may be null if desired
                return
            toDoList.add_task(title, descrip, due)
            self.refresh_tasks()

    def complete_task(self, title):
        if toDoList.deleteTask(title):
            QMessageBox.information(self.window, "Complete", f"'{title}' done!")
            self.refresh_tasks()

#main
if __name__ == "__main__":
    app = QApplication([])
    ui = MainWindow()
    ui.show()
    app.exec()
