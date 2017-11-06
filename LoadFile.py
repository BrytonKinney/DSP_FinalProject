from __future__ import print_function
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QFileDialog, QApplication)
import sys
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

class FinalProject(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    def initUI(self):
        self.btn = QPushButton('Open File', self)
        self.btn.move(275, 20)
        self.btn.clicked.connect(self.openFileNameDialog)

        self.le = QLineEdit(self)
        self.le.move(20, 22)
        self.le.setGeometry(20, 22, 205, 22)
        self.setGeometry(300, 300, 350, 120)
        self.setWindowTitle('Input dialog')
        self.show()

    def displaywaveform(self, filename):
        try:
            y, sr = librosa.load(filename)
            print(y)
            plt.figure()
            plt.subplot(2, 1, 1)
            plt.ylabel('Amplitude')
            plt.xlabel('Time')
            plt.title('Waveform')
            librosa.display.waveplot(y, sr=sr)
            plt.subplot(2, 1, 2)
            plt.ylabel('Amplitude')
            plt.xlabel('Time')
            plt.title('FFT')
           # D = librosa.amplitude_to_db(librosa.stft(y), ref=np.max)
           # librosa.display.specshow(D, sr=sr, y_axis='linear')
            librosa.display.specshow(np.fft.fftfreq(y), sr=sr)
            plt.show()
        except Exception as valErr:
            print(valErr.args)
    def openFileNameDialog(self):
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.ReadOnly
            fileName, _ = QFileDialog.getOpenFileName(self,"Select a sound file", "","All Files (*);;", options=options)
            if fileName:
                self.le.setText(fileName)
                self.displaywaveform(fileName)
        except Exception as valErr:
            print(valErr.args)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FinalProject()
    sys.exit(app.exec_())