from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QToolBar,
    QAction,
    QStatusBar,
)
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from panel import LabelPanel, ChartPanel, ButtonPanel
from menu import Menu
from toolbar import ToolBar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._window_init()
        self._toolbar_init()
        self._menu_init()
        self._main_area_init()
    
    def _window_init(self):
        self.setWindowTitle('My First PyQt5 App')
        self.setFixedSize(QSize(800, 600))

    def _menu_init(self):
        menu = Menu(self)

    def _toolbar_init(self):
        toolbar = ToolBar(self)

    def _main_area_init(self):
        self.layout = QVBoxLayout()
        self.layout2 = QHBoxLayout()

        chart_panel = ChartPanel()
        self.layout.addWidget(chart_panel.get_widget())
        button_panel = ButtonPanel()
        label_panel = LabelPanel()
        self.layout2.addWidget(button_panel.get_widget())
        self.layout2.addWidget(label_panel.get_widget())

        widget = QWidget()
        widget2 = QWidget()
        widget2.setLayout(self.layout2) 
        self.layout.addWidget(widget2)
        self.setCentralWidget(widget)
        widget.setLayout(self.layout)


def app_main_window():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    app_main_window()