from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(100, 100, 400, 600)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):

        # variables
        # count variable
        self.count = 0

        # start flag
        self.start = False

        # creating push button to get time in seconds
        button = QPushButton("Set time(s)", self)

        # setting geometry to the push button
        button.setGeometry(125, 100, 150, 50)

        # adding action to the button
        button.clicked.connect(self.get_seconds)

        # creating label to show the seconds
        self.label = QLabel("//TIMER//", self)

        # setting geometry of label
        self.label.setGeometry(100, 200, 200, 50)

        # setting border to the label
        self.label.setStyleSheet("border : 3px solid black")

        # setting font to the label
        self.label.setFont(QFont('Times', 15))

        # setting alignment ot the label
        self.label.setAlignment(Qt.AlignCenter)

        # creating start button
        start_button = QPushButton("Start", self)


        start_button.setGeometry(125, 350, 150, 40)

        # adding action to the button
        start_button.clicked.connect(self.start_action)

        # creating pause button
        pause_button = QPushButton("Pause", self)

        # setting geometry to the button
        pause_button.setGeometry(125, 400, 150, 40)

        # adding action to the button
        pause_button.clicked.connect(self.pause_action)

        # creating reset  button
        reset_button = QPushButton("Reset", self)

        # setting geometry to the button
        reset_button.setGeometry(125, 450, 150, 40)

        # adding action to the button
        reset_button.clicked.connect(self.reset_action)

        # creating a timer object
        timer = QTimer(self)

        # adding action to timer
        timer.timeout.connect(self.showTime)

        # update the timer every tenth second
        timer.start(100)

    # method called by timer
    def showTime(self):

        # checking if flag is true
        if self.start:
            # incrementing the counter
            self.count -= 1

            # timer is completed
            if self.count == 0:

                # making flag false
                self.start = False

                # setting text to the label
                self.label.setText("Completed !!!! ")

        if self.start:
            # getting text from count
            text = str(self.count / 10) + " s"

            # showing text
            self.label.setText(text)


  # method called by the push button
    def get_seconds(self):

        # making flag false
        self.start = False

        # getting seconds and flag
        second, done = QInputDialog.getInt(self, 'Seconds', 'Enter Seconds:')

        # if flag is true
        if done:
            # changing the value of count
            self.count = second * 10

            # setting text to the label
            self.label.setText(str(second))



    def start_action(self):
        # making flag true
        self.start = True

        # count = 0
        if self.count == 0:
            self.start = False

    def pause_action(self):

        # making flag false
        self.start = False

    def reset_action(self):

        # making flag false
        self.start = False

        # setting count value to 0
        self.count = 0

        # setting label text
        self.label.setText("//TIMER//")



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
