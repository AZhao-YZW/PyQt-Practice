from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLayout
from typing import Optional, List

class WidgetNode:
    def __init__(self, widget: QWidget, widget_name: str, layout: QLayout,
                 parent: Optional[QWidget], parent_name: Optional[str]):
        self.widget = widget
        self.widget_name = widget_name
        self.layout = layout
        self.parent = parent
        self.parent_name = parent_name

class ELNode:
    widget: QWidget
    widget_name: str
    parent_name: Optional[str]
    layout_type: Optional[str]

class ELList:
    el_list: List[List[ELNode]]

class EasyLayout:
    DEFAULT_TOP_NAME = 'top_widget'

    def __init__(self, top: QWidget, layout_type: str = 'v', top_name: str = DEFAULT_TOP_NAME):
        widget_node = WidgetNode(top, top_name, self._get_layout(layout_type),
                                 None, None)
        widget_node.widget.setLayout(widget_node.layout)
        self._layout_list = [widget_node]
        self._top_name = top_name

    def _get_layout(self, layout_type: str):
        if layout_type == 'v':
            return QVBoxLayout()
        else:
            return QHBoxLayout()

    def _is_name_exist(self, name: str):
        for node in self._layout_list:
            if name == node.widget_name:
                return True
        return False

    def _get_widget(self, name: Optional[str]):
        if name is None:
            return None
        for node in self._layout_list:
            if name == node.widget_name:
                return node.widget
        raise ValueError('[EasyLayout] widget name [%s] not exist.' % name)

    def _get_widget_layout(self, name: str):
        for node in self._layout_list:
            if name == node.widget_name:
                return node.layout
        raise ValueError('[EasyLayout] widget name [%s] not exist.' % name)

    def _add_to_layout_list(self, node: WidgetNode):
        if self._is_name_exist(node.widget_name):
            print('[EasyLayout] add node failed, as widget name[%s] has exist.' % node.widget_name)
            return
        if node.parent is not None:
            parent_layout = self._get_widget_layout(node.parent_name)
            parent_layout.addWidget(node.widget)
        if node.widget.layout() is None:
            node.widget.setLayout(node.layout)
        self._layout_list.append(node)

    def add_widget(self, widget: QWidget, widget_name: str,
                   parent_name: Optional[str], layout_type: str = 'v'):
        widget_node = WidgetNode(widget, widget_name, self._get_layout(layout_type),
                                 self._get_widget(parent_name), parent_name)
        self._add_to_layout_list(widget_node)

    def add_muti_widgets(self, el_list: ELList, parent_top: bool = False):
        for el_node in el_list:
            if (parent_top is True) and (len(el_node) == 2):
                self.add_widget(*el_node, self._top_name)
            else:
                self.add_widget(*el_node)

    def get_top_name(self):
        return self._top_name
