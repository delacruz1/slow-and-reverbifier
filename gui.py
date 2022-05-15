import slowAndReverb
import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, QSlider, QHBoxLayout
from PySide6.QtCore import Qt

class SlowAndReverbifier(QWidget):
    def __init__(self):
        super().__init__()
        self.fileName = None
        self.speed = None
        self.roomSize = 0

        self.setWindowTitle("Slow and Reverbifier")
        self.setAcceptDrops(True)

        self.button = QPushButton("Hello")
        layout = QVBoxLayout()
        self.setLayout(layout)

        speedBox = QHBoxLayout()
        speedLabel = QLabel("Song Speed: ")
        self.speedSlider = QSlider(Qt.Horizontal, minimum=30000, maximum=40000)
        self.speedSlider.setTickPosition(QSlider.TicksBelow)
        self.speedSlider.setTickInterval(1000)
        self.speedSlider.setPageStep(1000)
        self.speedSlider.valueChanged.connect(self._speedChanged)

        speedBox.addWidget(speedLabel)
        speedBox.addWidget(self.speedSlider)
        layout.addLayout(speedBox)

    def _speedChanged(self, value):
        print(value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    sr = SlowAndReverbifier()
    sr.show()
    sys.exit(app.exec())