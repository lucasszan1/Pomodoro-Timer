from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt
from buttonsCss import butons_style

class TimerControls(QWidget):
    def __init__(self, timer_widget):
        super().__init__()
        self.timer_widget = timer_widget
        
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.botao_iniciar = self.button_creation("Iniciar",self.timer_widget.start_timer)
        self.botao_pausar = self.button_creation("Pausar",self.timer_widget.stop_timer)
        self.botao_resetar = self.button_creation("Resetar",self.timer_widget.reset_timer)

        layout.addWidget(self.botao_iniciar)
        layout.addWidget(self.botao_pausar)
        layout.addWidget(self.botao_resetar)

    def button_creation(self, texto, callback):
        botao = QPushButton(texto)
        botao.setFixedSize(600,60)
        botao.setStyleSheet(butons_style)
        botao.clicked.connect(callback)
        return botao
