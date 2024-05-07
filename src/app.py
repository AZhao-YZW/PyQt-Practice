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
from panel import LabelPanel, ChartPanel, ButtonPanel, DataPanel
from menu import Menu
from toolbar import ToolBar
from navigation import TabNav

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
        '''
        w_main_area [QVBoxLayout] (top)
        |-- w_tab_nav
        |-- (w_tab_1) [QVBoxLayout] (其由w_tab_nav管理, 不加入w_main_area)
            |-- w_panel [QVBoxLayout]
                |-- w_chart_panel
                |-- w_panel_sub_1 [QHBoxLayout]
                    |-- w_button_panel
                    |-- w_label_panel
        |-- (w_tab_2) [QVBoxLayout]
            |-- w_data_panel
        '''
        # component
        tab_nav = TabNav()
        chart_panel = ChartPanel()
        button_panel = ButtonPanel()
        label_panel = LabelPanel()
        data_panel = DataPanel()
        # layout
        layout_main = QVBoxLayout()
        layout_tab_1 = QVBoxLayout()
        layout_tab_2 = QVBoxLayout()
        layout_panel = QVBoxLayout()
        layout_panel_sub_1 = QHBoxLayout()
        # widget
        w_main_area = QWidget()
        w_panel = QWidget()
        w_panel_sub_1 = QWidget()
        w_tab_1 = tab_nav.get_tab_widget('Tab1')
        w_tab_2 = tab_nav.get_tab_widget('Tab2')
        w_main_area.setLayout(layout_main)
        w_panel.setLayout(layout_panel)
        w_panel_sub_1.setLayout(layout_panel_sub_1)
        w_tab_1.setLayout(layout_tab_1)
        w_tab_2.setLayout(layout_tab_2)
        w_tab_nav = tab_nav.get_widget()
        w_chart_panel = chart_panel.get_widget()
        w_button_panel = button_panel.get_widget()
        w_label_panel = label_panel.get_widget()
        w_data_panel = data_panel.get_widget()
        # set widget
        self.setCentralWidget(w_main_area)
        layout_main.addWidget(w_tab_nav)
        layout_tab_1.addWidget(w_panel)
        layout_panel.addWidget(w_chart_panel)
        layout_panel.addWidget(w_panel_sub_1)
        layout_panel_sub_1.addWidget(w_button_panel)
        layout_panel_sub_1.addWidget(w_label_panel)
        layout_tab_2.addWidget(w_data_panel)

def app_main_window():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    app_main_window()