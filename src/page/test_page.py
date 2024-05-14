from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QWidget
from typing import List
from panel import LabelPanel, ChartPanel, ButtonPanel
from base import EasyLayout, ELList

class TestPage:
    '''
    test_page [QVBoxLayout]
    |-- chart_panel
    |-- sub_panel [QHBoxLayout]
        |-- button_panel
        |-- label_panel
    '''
    def __init__(self):
        # top widget
        self.w_test_page = QWidget()
        # component
        chart_panel = ChartPanel()
        button_panel = ButtonPanel()
        label_panel = LabelPanel()
        # easy layout list
        el_list: ELList = [
            [chart_panel.get_widget(),  'chart_panel',  'test_page'     ],
            [QWidget(),                 'sub_panel',    'test_page', 'h'],
            [button_panel.get_widget(), 'button_panel', 'sub_panel'     ],
            [label_panel.get_widget(),  'label_panel',  'sub_panel'     ],
        ]
        # easy layout
        easy_layout = EasyLayout(self.w_test_page, 'test_page', 'v')
        easy_layout.add_muti_widgets(el_list)
    
    def get_widget(self):
        return self.w_test_page