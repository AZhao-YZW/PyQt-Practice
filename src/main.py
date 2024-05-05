# PyQt5 main module: QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
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

if __name__ == '__main__':
    pyqt5_start()