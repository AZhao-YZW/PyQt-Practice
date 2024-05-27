from PySide6.QtWidgets import QStatusBar, QMainWindow
from base import PublicAction

class Menu:
    def __init__(self, window: QMainWindow):
        public_action = PublicAction(window)
        self.button_action = public_action.get_button_action()
        self.button_action2 = public_action.get_button_action2()
        window.setStatusBar(QStatusBar(window))
        self.menu = window.menuBar()
        file_menu = self.menu.addMenu("&File")
        file_menu.addAction(self.button_action)
        file_menu.addSeparator()
        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(self.button_action2)
    
    def get_widget(self):
        return self.menu