from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QAction, QIcon

class PublicAction:
    def __init__(self, window: QMainWindow):
        self.button_action = QAction(QIcon("fruit.png"), "&Your button", window)
        self.button_action.setStatusTip("This is your button")
        self.button_action.triggered.connect(self.onMyToolBarButtonClick)
        self.button_action.setCheckable(True)
        self.button_action2 = QAction(QIcon("fruit.png"), "Your &button2", window)
        self.button_action2.setStatusTip("This is your button2")
        self.button_action2.triggered.connect(self.onMyToolBarButtonClick)
        self.button_action2.setCheckable(True)
    
    def get_button_action(self):
        return self.button_action
    
    def get_button_action2(self):
        return self.button_action2
    
    def onMyToolBarButtonClick(self, s):
        print("click", s)