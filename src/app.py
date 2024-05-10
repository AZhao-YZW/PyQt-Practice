from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
)
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from typing import List, Optional
from panel import LabelPanel, ChartPanel, ButtonPanel, DataPanel
from menu import Menu
from toolbar import ToolBar
from navigation import TabNav
from base import EasyLayout

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
        # component
        tab_nav = TabNav()
        chart_panel = ChartPanel()
        button_panel = ButtonPanel()
        label_panel = LabelPanel()
        data_panel = DataPanel()
        # widget
        w_main_area = QWidget()
        # layout list
        '''
        main_area [QVBoxLayout] (top)
        |-- tab_nav
        |-- (tab_1) [QVBoxLayout] (其由tab_nav管理, 不加入main_area)
            |-- panel [QVBoxLayout]
                |-- chart_panel
                |-- panel_sub_1 [QHBoxLayout]
                    |-- button_panel
                    |-- label_panel
        |-- (tab_2) [QVBoxLayout]
            |-- data_panel
        '''
        layout_list: List[List[QWidget, str, Optional[str], Optional[str]]] = [
            [tab_nav.get_widget(),           'tab_nav',      'main_area'      ],
            [tab_nav.get_tab_widget('Tab1'), 'tab_1',        None,         'v'],
            [QWidget(),                      'panel',        'tab_1',      'v'],
            [chart_panel.get_widget(),       'chart_panel',  'panel'          ],
            [QWidget(),                      'panel_sub_1',  'panel',      'h'],
            [button_panel.get_widget(),      'button_panel', 'panel_sub_1'    ],
            [label_panel.get_widget(),       'label_panel',  'panel_sub_1'    ],
            [tab_nav.get_tab_widget('Tab2'), 'tab_2',        None,         'v'],
            [data_panel.get_widget(),        'data_panel',   'tab_2'          ],
        ]
        # easy layout
        easy_layout = EasyLayout(w_main_area, 'main_area', 'v')
        for layout in layout_list:
            if len(layout) == 4:
                easy_layout.add_widget(layout[0], layout[1], layout[2], layout[3])
            else:
                easy_layout.add_widget(layout[0], layout[1], layout[2])
        self.setCentralWidget(w_main_area)

def app_main_window():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    app_main_window()