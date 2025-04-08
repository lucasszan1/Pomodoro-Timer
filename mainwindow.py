from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout)
class MainWindow(QMainWindow):
    def __init__(self,):
        super().__init__()

        # Layout
        self.cw = QWidget()
        self.layout_botoes = (QHBoxLayout)
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)

        # Nome da Janela
        self.setWindowTitle("Pomodoro Timer")

        # Ajuste do tamanho da janela
        self.showMaximized()

        #css
        self.setStyleSheet("background-color: #404040;")

    def addWidgetToVlayout(self, widget:QWidget):
        self.v_layout.addWidget(widget)

    def addLayoutToVlayout(self, layout):
        self.v_layout.addLayout(layout)



       