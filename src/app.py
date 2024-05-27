from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from base import EasyLayout, ELList, FlexWindow
from menu import Menu
from toolbar import ToolBar
from page import TestPage, TabNav
from panel import DataPanel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._window_init()
        self._toolbar_init()
        self._menu_init()
        self._main_area_init()
    
    def _window_init(self):
        flex_window = FlexWindow(self)
        flex_window.set_title('My First PySide6 App')
        # flex_window.set_fixed_size(QSize(800, 600))
        flex_window.set_flex_size(0.5, 0.5)
        # flex_window.set_frameless_theme()

    def _menu_init(self):
        menu = Menu(self)

    def _toolbar_init(self):
        toolbar = ToolBar(self)
    
    def _main_area_init(self):
        # top widget
        w_main_area = QWidget()
        # component
        tab_nav = TabNav(['Tab1', 'Tab2', 'Tab3'], 'Tab1', 'n', True)
        test_page = TestPage()
        data_panel = DataPanel()
        # easy layout list
        '''
        main_area [QVBoxLayout] (top)
        |-- tab_nav
        |-- (tab_1) [QVBoxLayout] (其由tab_nav管理, 不加入main_area)
            |-- test_page
        |-- (tab_2) [QVBoxLayout]
            |-- data_panel
        '''
        el_list: ELList = [
            [tab_nav.get_widget(),           'tab_nav',      'main_area'      ],
            [tab_nav.get_tab_widget('Tab1'), 'tab_1',        None,         'v'],
            [test_page.get_widget(),         'test_page',    'tab_1'          ],
            [tab_nav.get_tab_widget('Tab2'), 'tab_2',        None,         'v'],
            [data_panel.get_widget(),        'data_panel',   'tab_2'          ],
        ]
        # easy layout
        easy_layout = EasyLayout(w_main_area, 'v', 'main_area')
        easy_layout.add_muti_widgets(el_list)
        self.setCentralWidget(w_main_area)

def app_main_window():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    app_main_window()