from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from base import EasyLayout, ELList

class TestPage:
    '''
    test_page [QHBoxLayout]
    |-- colume_1 [QVBoxLayout]
        |-- text
        |-- button
        |-- picture
    |-- colume_2 [QVBoxLayout]
        |-- input
        |-- list
    |-- colume_3 [QVBoxLayout]
        |-- chart
        |-- muti_select
        |-- single_select
    '''
    def __init__(self):
        # top widget
        self.w_test_page = QWidget()
        # easy layout list
        el_list: ELList = [
            [QWidget(), 'colume_1', 'test_page', 'v'],
            [QWidget(), 'colume_2', 'test_page', 'v'],
            [QWidget(), 'colume_3', 'test_page', 'v'],
            [self._get_text_widget(), 'text', 'colume_1'],
            [self._get_button_widget(), 'button', 'colume_1'],
            [self._get_picture_widget(), 'picture', 'colume_1'],
            [self._get_input_widget(), 'input', 'colume_2'],
            [self._get_list_widget(), 'list', 'colume_2'],
            [self._get_chart_widget(), 'chart', 'colume_3'],
            [self._get_muti_select_widget(), 'muti_select', 'colume_3'],
            [self._get_single_select_widget(), 'single_select', 'colume_3'],
        ]
        # easy layout
        easy_layout = EasyLayout(self.w_test_page, 'test_page', 'h')
        easy_layout.add_muti_widgets(el_list)
    
    def _get_text_widget(self):
        el_list: ELList = [
            [QLabel('静态文本：'), 'label_text'],
            [QLabel('text_1'), 'text_1'],
            [QLabel('text_2'), 'text_2'],
            [QLabel('text_3'), 'text_3'],
        ]
        return self._get_widget_common('v', el_list)
    
    def _get_button_widget(self):
        el_list: ELList = [
            [QLabel('按钮：'), 'label_button'],
            [QPushButton('button_1'), 'button_1'],
            [QPushButton('button_2'), 'button_2'],
            [QPushButton('button_3'), 'button_3'],
        ]
        return self._get_widget_common('v', el_list)
    
    def _get_picture_widget(self):
        el_list: ELList = [
            [QLabel('图像：'), 'label_picture'],
        ]
        return self._get_widget_common('v', el_list)
    
    def _get_input_widget(self):
        el_list: ELList = [
            [QLabel('输入框：'), 'label_input'],
        ]
        return self._get_widget_common('v', el_list)
    
    def _get_list_widget(self):
        el_list: ELList = [
            [QLabel('列表：'), 'label_list'],
        ]
        return self._get_widget_common('v', el_list)
    
    def _get_chart_widget(self):
        el_list: ELList = [
            [QLabel('图表：'), 'label_chart'],
        ]
        return self._get_widget_common('v', el_list)
    
    def _get_muti_select_widget(self):
        el_list: ELList = [
            [QLabel('多选框：'), 'label_m_select'],
        ]
        return self._get_widget_common('v', el_list)
    
    def _get_single_select_widget(self):
        el_list: ELList = [
            [QLabel('单选框：'), 'label_s_select'],
        ]
        return self._get_widget_common('v', el_list)
    
    def _get_widget_common(self, top_layout: str, el_list: ELList) -> QWidget:
        widget = QWidget()
        easy_layout = EasyLayout(widget, top_layout)
        easy_layout.add_muti_widgets(el_list, True)
        return widget

    def get_widget(self):
        return self.w_test_page