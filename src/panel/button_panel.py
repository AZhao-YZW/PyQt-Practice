from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget

class ButtonPanel:
    def __init__(self):
        self.layout = QVBoxLayout()
        btn1 = QPushButton()
        btn2 = QPushButton()
        btn3 = QPushButton()      
        btn1.setText('button 1')
        btn2.setText('button 2')
        btn3.setText('button 3')
        self.layout.addStretch(1)
        self.layout.addWidget(btn1)
        self.layout.addStretch(1)
        self.layout.addWidget(btn2)
        self.layout.addStretch(1)
        self.layout.addWidget(btn3)
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
    
    def get_widget(self):
        return self.widget