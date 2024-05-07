from typing import Dict
from PyQt5.QtWidgets import QTabWidget, QLabel, QWidget

class TabNav:
    _tab_list: Dict[str, QWidget] = {}

    def __init__(self):
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.North)
        self.tabs.setMovable(True)
        self._init_tab_list()
        for tab_name, widget in self._tab_list.items():
            self.tabs.addTab(widget, tab_name)
        self.tabs.setCurrentWidget(self._tab_list['Tab1'])

    def _init_tab_list(self):
        for tab_name in ['Tab1', 'Tab2', 'Tab3']:
            self._tab_list[tab_name] = QWidget()

    def get_widget(self):
        return self.tabs
    
    def get_tab_widget(self, tab_name: str):
        if tab_name in self._tab_list:
            return self._tab_list[tab_name]