from PyQt5.QtWidgets import QTabWidget, QWidget
from typing import Dict, List

class TabNav:
    def __init__(self, tab_list: List[str], start_tab: str, pos='n', movable=True):
        self._tab_table: Dict[str, QWidget] = {}
        self.tab_nav = QTabWidget()
        self.set_tab_pos(pos)
        self.tab_nav.setMovable(movable)
        for name in tab_list:
            self.add_new_tab(name)
        if tab_list != [] and (start_tab in tab_list):
            self.tab_nav.setCurrentWidget(self._tab_table[start_tab])
        else:
            print('start_tab[%s] is not in tab_list, default first tab' % start_tab)

    def add_new_tab(self, name: str):
        widget = QWidget()
        self.tab_nav.addTab(widget, name)
        self._tab_table[name] = widget

    def set_tab_pos(self, pos: str):
        '''
        pos valid value contains n|s|e|w,
        if pos not in valid value, pos default set to n
        '''
        tab_nav_pos = QTabWidget.TabPosition.North
        if pos == 'n':
            tab_nav_pos = QTabWidget.TabPosition.North
        elif pos == 's':
            tab_nav_pos = QTabWidget.TabPosition.South
        elif pos == 'e':
            tab_nav_pos = QTabWidget.TabPosition.East
        elif pos == 'w':
            tab_nav_pos = QTabWidget.TabPosition.West
        self.tab_nav.setTabPosition(tab_nav_pos)

    def get_widget(self):
        return self.tab_nav
    
    def get_tab_widget(self, name: str):
        if name in self._tab_table:
            return self._tab_table[name]