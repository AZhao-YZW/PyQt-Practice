from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLayout
from typing import List, Optional


class WidgetNode:
    widget: QWidget
    widget_name: str
    layout: QLayout
    parent: QWidget
    parent_name: str


class EasyLayout:
    def __init__(self, top: QWidget, top_name: str, layout: str = 'v'):
        widget_node = WidgetNode()
        widget_node.widget = top
        widget_node.widget_name = top_name
        widget_node.layout = self._get_layout_type(layout)
        widget_node.parent = None
        widget_node.parent_name = None
        widget_node.widget.setLayout(widget_node.layout)
        self._layout_list = [widget_node]

    def _get_layout_type(self, layout: str):
        if layout == 'v':
            return QVBoxLayout()
        else:
            return QHBoxLayout()

    def _is_name_in_layout_list(self, name: str) -> bool:
        for node in self._layout_list:
            if name == node.widget_name:
                return True
        return False

    def _get_widget(self, name: Optional[str]) -> QWidget:
        if name is None:
            return None
        for node in self._layout_list:
            if name == node.widget_name:
                return node.widget
        raise ValueError('[EasyLayout] widget name [%s] not exist.' % name)

    def _get_widget_layout(self, name: str) -> QLayout:
        for node in self._layout_list:
            if name == node.widget_name:
                return node.layout
        raise ValueError('[EasyLayout] widget name [%s] not exist.' % name)

    def _add_to_layout_list(self, node: WidgetNode):
        if self._is_name_in_layout_list(node.widget_name):
            print('[EasyLayout] add node failed, as widget name has exist.')
            return
        if node.parent is not None:
            parent_layout = self._get_widget_layout(node.parent_name)
            parent_layout.addWidget(node.widget)
        node.widget.setLayout(node.layout)
        self._layout_list.append(node)

    def add_widget(self, widget: QWidget, widget_name: str, parent_name: Optional[str], layout: str = 'v'):
        widget_node = WidgetNode()
        widget_node.widget = widget
        widget_node.widget_name = widget_name
        widget_node.layout = self._get_layout_type(layout)
        widget_node.parent = self._get_widget(parent_name)
        widget_node.parent_name = parent_name
        self._add_to_layout_list(widget_node)

    _layout_list: List[WidgetNode] = []
