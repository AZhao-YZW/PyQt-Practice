# PyQt5 main module: QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtCore import QSize, Qt
import sys

def pyqt5_start():
    app = QApplication(sys.argv)    # uniqe for each application
    window = QWidget()              # window is the top level, app need at least one
    window.show()                   # window is default invisible
    window2 = QPushButton('Click')  # any widget can be window
    window2.show()
    window3 = QMainWindow()         # window that provides standard feature
    window3.show()
    app.exec()                      # start up the event loop (also uniqe for app)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MainWindow Test')
        # button
        button = QPushButton('Push me')
        button.setCheckable(True)   # 'True' is like a switch
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)
        # button2
        self.button2 = QPushButton('Self Signal')
        self.button2.setCheckable(True)
        self.button2.clicked.connect(self.the_button_was_released)
        # button3
        self.button3 = QPushButton('Update widget status')
        self.button3.setCheckable(True)
        self.button3.clicked.connect(self.the_button_click_once)
        # most widget has available slot
        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(button)
        self.setCentralWidget(self.button2)
        self.setCentralWidget(self.button3)
    
    def the_button_was_clicked(self):
        print('Clicked!')
    
    def the_button_was_toggled(self, checked):
        print('Clicked?', checked)

    def the_button_was_released(self):
        print('Released?', not self.button2.isChecked())
    
    def the_button_click_once(self):
        self.button3.setText('Already clicked')
        self.button3.setEnabled(False)
        self.setWindowTitle('button3 clicked')

def pyqt5_main_window():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    pyqt5_main_window()