import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout)
from PySide6.QtCore import Qt
from mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()


    label_texte = QLabel("blabla")
    window.addWidgetToVlayout(label_texte)
    label_texte.setAlignment(Qt.AlignmentFlag.AlignCenter)


    # Botoes

    layout_botoes = QVBoxLayout()


    botao_iniciar = QPushButton("Iniciar")
    botao_pausar = QPushButton("Pausar")
    botao_resetar = QPushButton("Resetar")

    botao_iniciar.setFixedSize(200,40)
    botao_pausar.setFixedSize(200,40)
    botao_resetar.setFixedSize(200,40)

    layout_botoes.setStretch(0,0 )
    layout_botoes.addWidget(botao_iniciar)
    layout_botoes.addWidget(botao_pausar)
    layout_botoes.addWidget(botao_resetar)
    layout_botoes.setStretch(0, 0)
    layout_botoes.setAlignment(Qt.AlignmentFlag.AlignCenter)

    window.addLayoutToVlayout(layout_botoes)


    # Qss botoes
    botao_iniciar.setStyleSheet("""
        color: #FFFFFF;
        font-size: 20px;   
        border: 2px solid #181818;     
        border-radius:20px;    
        background-color: #282828; 
                     
""")
    botao_pausar.setStyleSheet("""
        color: #FFFFFF;
        font-size: 20px;   
        border: 2px solid #181818;     
        border-radius:20px;    
        background-color: #282828;               
""")
    botao_resetar.setStyleSheet("""
        color: #FFFFFF;
        font-size: 20px;   
        border: 2px solid #181818;     
        border-radius:20px;    
        background-color: #282828;               
""")

    # Executa
    window.show()
    app.exec()

