import sys
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
from timer import  TimerPomodoro
from timercontrols import TimerControls

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    timer_widget= TimerPomodoro()
    controls = TimerControls(timer_widget)

    main_window.addWidgetToVlayout(timer_widget)  
    main_window.addWidgetToVlayout(controls)

    main_window.show()
    app.exec()

