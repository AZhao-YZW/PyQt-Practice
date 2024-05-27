from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import Qt, QSize

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
        screen = QGuiApplication.primaryScreen()
        screen_rect = screen.geometry()
        height = int(screen_rect.height() * w_ratio)
        width = int(screen_rect.width() * h_ratio)
        self.main_window.resize(width, height)

    def set_frameless_theme(self):
        self.main_window.setWindowFlags(Qt.WindowType.Window |
                                        Qt.WindowType.FramelessWindowHint |
                                        Qt.WindowType.WindowSystemMenuHint |
                                        Qt.WindowType.WindowMinimizeButtonHint |
                                        Qt.WindowType.WindowMaximizeButtonHint)
        self.main_window.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
