from PyQt5.QtWidgets import *
from MusicPlayer import Pencere
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())