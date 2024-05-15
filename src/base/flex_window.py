from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QSize

class FlexWindow:
    def __init__(self, main_window: QMainWindow):
        self.main_window = main_window

    def set_title(self, title: str):
        self.main_window.setWindowTitle(title)
    
    def set_fixed_size(self, size: QSize):
        self.main_window.setFixedSize(size)

    def set_flex_size(self, w_ratio: float, h_ratio: float):
        '''
        w_ratio and h_ratio is the ratio to screen
        '''
        desktop = QApplication.desktop()
        screen_rect = desktop.screenGeometry()
        height = int(screen_rect.height() * w_ratio)
        width = int(screen_rect.width() * h_ratio)
        self.main_window.resize(width, height)
