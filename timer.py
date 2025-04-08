from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import QTimer, QTime, Qt
from PySide6.QtGui import QFont, QFontDatabase
from playsound import playsound
import sys
import os


def resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

class TimerPomodoro(QWidget):
    def __init__(self):
        super().__init__()

        self.layout_timer = QVBoxLayout(self)
        self.working = True

        self.define_time()

        self.label_timer = QLabel(self.time_remainder.toString("hh:mm:ss"))
        self.label_timer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.font_path = resource_path("assets/fonte.ttf")
        font_id = QFontDatabase.addApplicationFont(self.font_path)
        family = QFontDatabase.applicationFontFamilies(font_id)

        if family:
            self.font = QFont(family[0], 110)  
            self.label_timer.setFont(self.font)

        self.label_timer.setStyleSheet("color:white;")

        self.timer = QTimer()
        self.timer.timeout.connect(self.time_changing)

        self.layout_timer.addWidget(self.label_timer)
        self.setLayout(self.layout_timer)

    def define_time(self):
        if self.working:
            self.time_remainder = QTime(0, 25, 0)
        else:
            self.time_remainder = QTime(0, 5, 0)

    def start_timer(self):
        self.timer.start(1000)

    def stop_timer(self):
        self.timer.stop()

    def reset_timer(self):
        self.working = True
        self.define_time()
        self.label_timer.setText(self.time_remainder.toString("hh:mm:ss"))

    def time_changing(self):
        self.time_remainder = self.time_remainder.addSecs(-1)
        self.label_timer.setText(self.time_remainder.toString("hh:mm:ss"))

        if self.time_remainder == QTime(0, 0, 0):
            self.cycle_changing()
            self.playmusica()


    def cycle_changing(self):
        self.working = not self. working
        self.define_time()
        self.label_timer.setText(self.time_remainder.toString("hh:mm:ss"))
        self.timer.start(1000)

    def playmusica(self):
        self.caminho_som = resource_path("assets/som.wav")
        playsound(self.caminho_som)


 