import sys
import os
from slowAndReverb import processAudio
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import (
    QApplication, 
    QLabel, 
    QPushButton, 
    QMessageBox, 
    QVBoxLayout, 
    QWidget, 
    QSlider, 
    QHBoxLayout, 
    QFileDialog,
)


class SlowAndReverbifier(QWidget):
    def __init__(self):
        super().__init__()
        self._setUpInterface()
    
    def _setUpInterface(self):
    
        # Song Configuration Choices
        self.speedAmounts = [
                38000, 
                39000, 
                40000, 
                41000,
                42000, 
                43000, 
                44000, 
                45000, 
                46000, 
                47000
        ]
        self.reverbAmounts = [
            0.0, 
            0.10, 
            0.25, 
            0.5
        ]

        self.fileName = None
        self.speed = self.speedAmounts[0]
        self.roomSize = self.reverbAmounts[0]

        # Window Layout Setup
        self.resize(600, 200)
        center = QGuiApplication.screens()[0].geometry().center()
        self.move(center - self.frameGeometry().center())
        self.setWindowTitle("Slow and Reverbifier")
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Song Picker
        self.fileLabel = QLabel(f'File Selected: {self.fileName}')
        layout.addWidget(self.fileLabel)
        self.fileButton= QPushButton("Choose a Song (in .wav format)")
        self.fileButton.clicked.connect(self._getFile)
        layout.addWidget(self.fileButton)

        # Song Speed Picker
        speedBox = QHBoxLayout()
        speedLabel = QLabel("Song Speed: ")
        self.speedSlider = QSlider(Qt.Horizontal, minimum=0, maximum=len(self.speedAmounts)-1)
        self.speedSlider.setTickPosition(QSlider.TicksBothSides)
        self.speedSlider.setTickInterval(1)
        self.speedSlider.setSingleStep(1)
        self.speedSlider.valueChanged.connect(self._speedChanged)

        speedBox.addWidget(speedLabel)
        speedBox.addWidget(self.speedSlider)
        layout.addLayout(speedBox)

        # Reverb Room Size Picker
        reverbBox = QHBoxLayout()
        reverbLabel = QLabel("Reverb Amount: ")
        self.reverbSlider = QSlider(Qt.Horizontal, minimum=0, maximum=len(self.reverbAmounts)-1)
        self.reverbSlider.setTickPosition(QSlider.TicksBothSides)
        self.reverbSlider.setTickInterval(1)
        self.reverbSlider.setSingleStep(1)
        self.reverbSlider.valueChanged.connect(self._reverbChanged)

        reverbBox.addWidget(reverbLabel)
        reverbBox.addWidget(self.reverbSlider)
        layout.addLayout(reverbBox)

        # Slow and Reverb Button
        self.slowAndReverbButton = QPushButton("Slow and Reverbify!")
        self.slowAndReverbButton.setEnabled(False)
        self.slowAndReverbButton.clicked.connect(lambda: processAudio(self.fileName, self.roomSize, self.speed))
        
        if self.fileName:
            self.slowAndReverbButton.setEnabled(True)
        layout.addWidget(self.slowAndReverbButton)

    # File Dialog Helper
    def _getFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './', "Wav file (*.wav)")
        self.fileName = fname[0]
        self.fileLabel.setText(f'File Selected: {os.path.basename(fname[0])}')
        if fname:
            self.slowAndReverbButton.setEnabled(True)

    # Speed Changer Helper
    def _speedChanged(self, value):
        self.speed = self.speedAmounts[value]
    
    # Reverb Room Size Helper
    def _reverbChanged(self, value):
        self.roomSize = self.reverbAmounts[value]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    sr = SlowAndReverbifier()
    sr.show()
    sys.exit(app.exec())