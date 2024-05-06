from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget

class LabelPanel:
    def __init__(self):
        self.layout = QVBoxLayout()
        label1 = QLabel()
        label2 = QLabel()
        label3 = QLabel()      
        label1.setText('label 1')
        label2.setText('label 2')
        label3.setText('label 3')
        self.layout.addStretch(1)
        self.layout.addWidget(label1)
        self.layout.addStretch(1)
        self.layout.addWidget(label2)
        self.layout.addStretch(1)
        self.layout.addWidget(label3)
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
    
    def get_widget(self):
        return self.widget