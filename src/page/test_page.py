from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QCheckBox, QLineEdit,
    QListWidget, QRadioButton
)
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
from base import EasyLayout, ELList, EventMaster
from panel import ChartPanel
import subprocess, os

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
        easy_layout = EasyLayout(self.w_test_page, 'h', 'test_page')
        easy_layout.add_muti_widgets(el_list)
        # event master
        self._event_init()

    def _event_init(self):
        def on_click_button(label: QLabel):
            text = label
            content = text.text()
            splits = content.split(': ')
            if len(splits) == 1:
                new_content = content + ': 1'
            else:
                new_content = splits[0] + ': ' + str(int(splits[1]) + 1)
            text.setText(new_content)
            app_path = os.getcwd()
            subprocess.run(['python', app_path + '/script/print_hello.py'])
        
        event_master = EventMaster()
        event_master.set_subject('button_1', self.button_1.clicked.connect)
        event_master.set_observer('text_1', 'button_1', on_click_button, [self.text_1])
        event_master.set_subject('button_2', self.button_2.clicked.connect)
        event_master.set_observer('text_2', 'button_2', on_click_button, [self.text_2])
        event_master.set_subject('button_3', self.button_3.clicked.connect)
        event_master.set_observer('text_3', 'button_3', on_click_button, [self.text_3])

    def _get_text_widget(self):
        self.text_1 = QLabel('text_1')
        self.text_2 = QLabel('text_2')
        self.text_3 = QLabel('text_3')
        el_list: ELList = [
            [QLabel('静态文本：'), 'label_text'],
            [self.text_1, 'text_1'],
            [self.text_2, 'text_2'],
            [self.text_3, 'text_3'],
        ]
        return self._get_widget_common('v', el_list)

    def _get_button_widget(self):
        self.button_1 = QPushButton('button_1')
        self.button_2 = QPushButton('button_2')
        self.button_3 = QPushButton('button_3')
        el_list: ELList = [
            [QLabel('按钮：'), 'label_button'],
            [self.button_1, 'button_1'],
            [self.button_2, 'button_2'],
            [self.button_3, 'button_3'],
        ]
        return self._get_widget_common('v', el_list)

    def _get_picture_widget(self):
        el_list: ELList = [
            [QLabel('静态图像：'), 'label_picture'],
        ]
        return self._get_widget_common('v', el_list)

    def _get_input_widget(self):
        el_list: ELList = [
            [QLabel('输入框：'), 'label_input'],
            [QLineEdit(), 'input'],
        ]
        return self._get_widget_common('v', el_list)

    def _get_list_widget(self):
        list_widget = QListWidget()
        list_widget.addItems(['Apple', 'Pear', 'Banana'])
        el_list: ELList = [
            [QLabel('列表：'), 'label_list'],
            [list_widget, 'list'],
        ]
        return self._get_widget_common('v', el_list)

    def _get_chart_widget(self):
        el_list: ELList = [
            [QLabel('图表：'), 'label_chart'],
            [ChartPanel().get_widget(), 'chart'],
        ]
        return self._get_widget_common('v', el_list)

    def _get_muti_select_widget(self):
        el_list: ELList = [
            [QLabel('多选框：'), 'label_m_select'],
            [QWidget(), 'example', EasyLayout.DEFAULT_TOP_NAME, 'h'],
            [QCheckBox('选项1'), 'item_1', 'example'],
            [QCheckBox('选项2'), 'item_2', 'example'],
            [QCheckBox('选项3'), 'item_3', 'example'],
        ]
        return self._get_widget_common('v', el_list)

    def _get_single_select_widget(self):
        # QRadioButton在同一个layout下视为同一组
        item_A = QRadioButton('选项A')
        item_B = QRadioButton('选项B')
        item_C = QRadioButton('选项C')
        item_D = QRadioButton('选项D')
        item_E = QRadioButton('选项E')
        item_F = QRadioButton('选项F')
        el_list: ELList = [
            [QLabel('单选框：'), 'label_s_select'],
            [QLabel('第1题：'), 'label_1'],
            [QWidget(), 'example_1', EasyLayout.DEFAULT_TOP_NAME, 'h'],
            [item_A, 'item_A', 'example_1'],
            [item_B, 'item_B', 'example_1'],
            [item_C, 'item_C', 'example_1'],
            [QLabel('第2题：'), 'label_2'],
            [QWidget(), 'example_2', EasyLayout.DEFAULT_TOP_NAME, 'h'],
            [item_D, 'item_D', 'example_2'],
            [item_E, 'item_E', 'example_2'],
            [item_F, 'item_F', 'example_2'],
        ]
        return self._get_widget_common('v', el_list)

    def _get_widget_common(self, top_layout: str, el_list: ELList) -> QWidget:
        widget = QWidget()
        easy_layout = EasyLayout(widget, top_layout)
        easy_layout.add_muti_widgets(el_list, True)
        return widget

    def get_widget(self):
        return self.w_test_page
