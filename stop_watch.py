import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

from PyQt5.QtCore import QTimer, QTime, Qt


class Stop_Watch(QWidget):
    def __init__(self):
        super(). __init__()

        self.time = QTime(0, 0, 0, 0)  # Storing time

        self.time_label = QLabel("00:00:00:00", self)
        self.start_button = QPushButton("START", self)
        self.stop_button = QPushButton("STOP", self)
        self.reset_button = QPushButton("RESET", self)

        self.timer = QTimer()

        self.initUI()

    def initUI(self):
        self.setGeometry(600, 400, 600, 200)
        self.setWindowTitle("STOP WATCH")

        # Layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.start_button.setCursor(Qt.PointingHandCursor)
        self.stop_button.setCursor(Qt.PointingHandCursor)
        self.reset_button.setCursor(Qt.PointingHandCursor)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)

        self.timer.timeout.connect(self.update_display)

        self.setStyleSheet("""
            QPushButton, QLabel{
                padding: 20px;
                font-weight: bold;
                           
            }               
            QPushButton{
                font-size: 50px;
                background-color: black;
                color: #0ad118;
                font-family: calibri;  
                border-radius: 20px;
                }
                           
            QPushButton:hover {
                background-color: #252926;         
                           }
            QLabel{
                font-size: 120px;
                background-color: black;
                color: #0ad118;
                font-family: calibri;
                border-radius: 25px;
                }
        """)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format(self.time))

    def format(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10

        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self):

        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format(self.time))


def main():
    app = QApplication(sys.argv)
    stop_watch = Stop_Watch()

    stop_watch.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
