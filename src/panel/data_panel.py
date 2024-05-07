from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QWidget

class DataPanel:
    def __init__(self):
        '''
        w_top [QHBoxLayout] (top)
        |-- w_left [QVBoxLayout]
            |-- w_label_1
            |-- w_label_2
            |-- w_label_3
        |-- w_right [QVBoxLayout]
            |-- w_label_4
            |-- w_label_5
            |-- w_label_6
        '''
        # layout
        layout_top = QHBoxLayout()
        layout_left = QVBoxLayout()
        layout_right = QVBoxLayout()
        # widget
        self.w_top = QWidget()
        w_left = QWidget()
        w_right = QWidget()
        self.w_top.setLayout(layout_top)
        w_left.setLayout(layout_left)
        w_right.setLayout(layout_right)
        w_label_1 = QLabel('label 1')
        w_label_2 = QLabel('label 2')
        w_label_3 = QLabel('label 3')
        w_label_4 = QLabel('label 4')
        w_label_5 = QLabel('label 5')
        w_label_6 = QLabel('label 6')
        # set widget
        layout_top.addWidget(w_left)
        layout_top.addWidget(w_right)
        layout_left.addWidget(w_label_1)
        layout_left.addWidget(w_label_2)
        layout_left.addWidget(w_label_3)
        layout_right.addWidget(w_label_4)
        layout_right.addWidget(w_label_5)
        layout_right.addWidget(w_label_6)
    
    def get_widget(self):
        return self.w_top