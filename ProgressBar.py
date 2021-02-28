import sys
import time

from PyQt5.QtCore import QThread, pyqtSignal, QWaitCondition, QMutex


class ProgressBar(QThread):
    countChanged = pyqtSignal(int)
    stopSignal = pyqtSignal(str)
    musicLengthSignal = pyqtSignal(int)
    setCountPosition = pyqtSignal(int)
    moveToTheNextMusic = pyqtSignal(int) #Let's say, when we signal integer 1337 signal, that would mean that the current song is finished playing.

    def __init__(self, parent=None):
        super().__init__(parent)
        self.musicLengthSignal.connect(self.progressBarMusicLength)

    def run(self):
        self.count = 0
        self.mtx = QMutex()
        self.wCndt = QWaitCondition()
        self.continueToSend = True
        while self.count < self.musicLength:
            self.stopSignal.connect(self.stopProgressBar)
            self.setCountPosition.connect(self.settingUpCount)
            if not self.continueToSend:
                self.mtx.lock()
                try:
                    self.wCndt.wait(self.mtx)
                finally:
                    self.mtx.unlock()
            else:
                self.count += 1
                time.sleep(1)
                self.countChanged.emit(self.count)
        self.moveToTheNextMusic.emit(1337) #It means that the current song has finished playing.

    def stop(self):
        self.terminate()

    def settingUpCount(self, countVal):
        self.count = countVal

    def stopProgressBar(self, cSignal):
        if cSignal == "stop":
            self.continueToSend = False

    def progressBarMusicLength(self, musicLength):
        self.musicLength = musicLength