from __future__ import print_function
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QFileDialog, QApplication)
import sys
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sc

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
        self.le.setGeometry(20, 22, 250, 22)
        self.setGeometry(300, 300, 370, 100)
        self.setWindowTitle('Input dialog')
        self.show()

    def displaywaveform(self, filename):
        try:
            y, sr = librosa.load(filename)
            print(y)
            signalLength = y.shape[0]
            plt.figure()
            plt.subplot(2, 2, 1)
            plt.ylabel('Amplitude')
            plt.xlabel('Time')
            plt.title('Waveform')
            librosa.display.waveplot(y, sr=sr)
            plt.subplot(2, 2, 2)
            plt.ylabel('|Amplitude|')
            plt.xlabel('Frequency (Hz)')
            print(signalLength)
            n = len(y)
            k = np.arange(n)
            T = n/sr
            frq = k/T
            print(n)
            print(n/2)
            print(range(int(n/2)))
            frq = frq[range(int(n/2))]
            Y = np.fft.fft(y)/n
            Y = Y[range(int(n/2))]
            plt.plot(frq, np.abs(Y))
            plt.xlabel('Frequency (Hz)')
            plt.xlim(auto=True)
            plt.ylabel('|Amplitude|')
            plt.subplot(2, 2, 3)
            plt.xlabel('Frequency (Hz)')
            plt.ylabel('Phase Angle')
            plt.plot(frq, np.angle(Y))
            #t = np.linspace(0, 2*np.pi)
            #dt = t[1] - t[0]
            #fa = 1.0/dt
            #plt.subplot(2, 1, 2)
            #Y = np.fft.fft(y)
            #N = int(np.round(len(Y)/2)) + 1
            #print(N)
            #Y[N-4:N+3]
            #X = np.linspace(0, fa/2, N, endpoint=True)
            #X[:4]
            #hann = np.hanning(signalLength)
            #Yhann = np.fft.fft(y*hann)
            #plt.plot(X, 2.0*np.abs(Yhann[:N])/N)
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