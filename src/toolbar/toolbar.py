from PyQt5.QtWidgets import QToolBar, QMainWindow, QLabel
from PyQt5.QtCore import QSize, Qt
from base import PublicAction

class ToolBar:
    def __init__(self, window: QMainWindow):
        public_action = PublicAction(window)
        self.button_action = public_action.get_button_action()
        self.button_action2 = public_action.get_button_action2()
        self.toolbar = QToolBar("My main toolbar")
        self.toolbar.setIconSize(QSize(16, 16))
        window.addToolBar(self.toolbar)
        self.toolbar.addAction(self.button_action)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.button_action2)
        self.toolbar.addWidget(QLabel("文字"))
    
    def get_widget(self):
        return self.toolbar