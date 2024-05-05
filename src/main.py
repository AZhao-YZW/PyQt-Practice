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
        button = QPushButton('Push me')
        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(button)

def pyqt5_main_window():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    pyqt5_main_window()