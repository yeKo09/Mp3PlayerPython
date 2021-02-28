import pygame
from Music import Music
import random
import os
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QPushButton,QLabel,QMainWindow,QSlider,QProgressBar,QAction,QHBoxLayout,QVBoxLayout,\
    QWidget,QMessageBox,QFileDialog,QTableWidgetItem,QTableWidget,qApp,QAbstractScrollArea
from PyQt5 import QtGui
import sys
import mysql.connector
from PyQt5.QtGui import QCursor
import webbrowser
from ProgressBar import ProgressBar

class Pencere(QMainWindow):

    def __init__(self):
        super().__init__()
        self.r_mode = 0
        self.initui()

    def initui(self):
        self.buton = QPushButton('Play')
        self.buton1 = QPushButton('Previous')
        self.buton2 = QPushButton('Next')
        self.buton3 = QPushButton('Delete')
        self.buton4 = QPushButton('Add Music')
        self.buton5 = QPushButton('Random Mode')

        self.buton.setIcon(QtGui.QIcon('C:\\Users\\yekta\\PycharmProjects\\music_player_python\\icons\\play_icon.png'))
        self.buton1.setIcon(QtGui.QIcon('C:\\Users\\yekta\\PycharmProjects\\music_player_python\\icons\\previous.png'))
        self.buton2.setIcon(QtGui.QIcon('C:\\Users\\yekta\\PycharmProjects\\music_player_python\\icons\\next.png'))
        self.buton3.setIcon(QtGui.QIcon('C:\\Users\\yekta\\PycharmProjects\\music_player_python\\icons\\delete.png'))
        self.buton4.setIcon(QtGui.QIcon('C:\\Users\\yekta\\PycharmProjects\\music_player_python\\icons\\addMusic2.png'))
        self.buton5.setIcon(QtGui.QIcon('C:\\Users\\yekta\\PycharmProjects\\music_player_python\\icons\\random.png'))

        self.buton.setCursor(QCursor(Qt.PointingHandCursor))
        self.buton1.setCursor(QCursor(Qt.PointingHandCursor))
        self.buton2.setCursor(QCursor(Qt.PointingHandCursor))
        self.buton3.setCursor(QCursor(Qt.PointingHandCursor))
        self.buton4.setCursor(QCursor(Qt.PointingHandCursor))
        self.buton5.setCursor(QCursor(Qt.PointingHandCursor))

        self.etiket2 = QLabel()
        self.etiket3 = QLabel()
        self.etiket4 = QLabel()
        self.etiket4.setPixmap(
            QtGui.QPixmap('C:\\Users\\yekta\\PycharmProjects\\music_player_python\\icons\\speaker.png'))
        self.etiket5 = QLabel()

        self.sp1 = QSlider(Qt.Horizontal, self)
        self.sp1.setMinimum(0)
        self.sp1.setMaximum(100)
        self.sp1.setSingleStep(25)
        self.sp1.setValue(25)
        self.sp1.setTickPosition(QSlider.TicksBelow)

        music = Music()
        self.createTable()
        self.fetchData(music)
        self.theChosenFile(music)

        #THIS SECTION IS FOR THE PROGRESS BAR : START
        self.pBar = QProgressBar()
        self.pBar.setTextVisible(False)
        self.timeLabel = QLabel()
        self.durationMusicLabel = QLabel()
        self.fifteenSecondBackwards = QPushButton('15sB')
        self.fifteenSecondBackwards.setCursor(QCursor(Qt.PointingHandCursor))
        self.fifteenSecondForwards = QPushButton('15sF')
        self.fifteenSecondForwards.setCursor(QCursor(Qt.PointingHandCursor))
        self.fifteenSecondBackwards.clicked.connect(lambda : self.setMusicPosition(music))
        self.fifteenSecondBackwards.setIcon(QtGui.QIcon('C:\\Users\\yekta\\PycharmProjects\\music_player_python\\icons\\rewind-arrow-draw.png'))
        self.fifteenSecondForwards.setIcon(
            QtGui.QIcon('C:\\Users\\yekta\\PycharmProjects\\music_player_python\\icons\\cycle-loading.png'))
        self.fifteenSecondForwards.clicked.connect(lambda : self.setMusicPosition(music))
        #: END



        menubar = self.menuBar()
        add = menubar.addMenu('Add')
        howTo = menubar.addMenu('How to')
        exit1 = menubar.addMenu('Exit')

        addMusic = QAction('Add Music', self)
        addMusic.setShortcut('Ctrl+O')

        addImage = QAction('Add Music Image', self)
        addImage.setShortcut('Ctrl+Y')

        howToUseThis = QAction('How to Use This Program?', self)
        howToUseThis.setShortcut('Ctrl+H')

        exitP = QAction('Exit the Program', self)
        exitP.setShortcut('Ctrl+Q')

        add.addAction(addMusic)
        add.addAction(addImage)
        howTo.addAction(howToUseThis)
        exit1.addAction(exitP)

        addMusic.triggered.connect(self.addMusic)
        addImage.triggered.connect(lambda: self.addMImage(music))
        howToUseThis.triggered.connect(self.howToUt)
        exitP.triggered.connect(self.exitTheProgram)

        #PROGRESS BAR SECTION : START
        h_pBox = QHBoxLayout()
        h_pBox.addStretch()
        h_pBox.addWidget(self.timeLabel)
        h_pBox.addWidget(self.pBar)
        h_pBox.addWidget(self.durationMusicLabel)
        h_pBox.addStretch()
        #: END

        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.etiket2)
        h_box.addWidget(self.etiket3)
        h_box.addStretch()
        h_box.addWidget(self.etiket5)
        h_box.addStretch()

        h_box2 = QHBoxLayout()
        h_box2.addStretch()
        h_box2.addWidget(self.table1)
        h_box2.addStretch()

        h_box3 = QHBoxLayout()
        h_box3.addStretch()
        h_box3.addWidget(self.buton5)
        h_box3.addWidget(self.buton1)
        h_box3.addWidget(self.fifteenSecondBackwards)
        h_box3.addWidget(self.buton)
        h_box3.addWidget(self.fifteenSecondForwards)
        h_box3.addWidget(self.buton2)
        h_box3.addWidget(self.etiket4)
        h_box3.addWidget(self.sp1)
        h_box3.addStretch()

        h_box4 = QHBoxLayout()
        h_box4.addStretch()
        h_box4.addWidget(self.buton4)
        h_box4.addWidget(self.buton3)
        h_box4.addStretch()

        v_box = QVBoxLayout()
        v_box.addLayout(h_box)
        #: START
        v_box.addLayout(h_pBox)
        #: END
        v_box.addLayout(h_box3)
        v_box.addStretch()
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box4)
        v_box.addStretch()

        self.setWindowTitle("YekoBox")
        self.setWindowIcon(QtGui.QIcon('C:\\Users\\yekta\\PycharmProjects\\music_player_python\\icons\\music_icon.png'))
        self.setGeometry(100, 40, 800, 600)
        window = QWidget()
        window.setLayout(v_box)
        self.setCentralWidget(window)

        self.buton.clicked.connect(lambda: self.clickToPlayMusic(music))
        self.buton1.clicked.connect(lambda: self.clickToPlayMusic(music))
        self.buton2.clicked.connect(lambda: self.clickToPlayMusic(music))
        self.buton3.clicked.connect(lambda: self.clickToPlayMusic(music))
        self.buton4.clicked.connect(self.addMusic)
        self.buton5.clicked.connect(lambda: self.random_mode(music))

        # CSS
        self.etiket2.setObjectName('playingInfo')
        self.setStyleSheet(open('style.css', 'r').read())

        self.show()

    def setMusicPosition(self, music):
        sender1 = self.sender()
        getTime = self.timeLabel.text()
        actualTimeInSeconds = 60 * int(getTime[0])
        # As we know, timer can be something like this 1:02 and i have to get that 02 to integer 2 for calculation purposes.
        if(int(getTime[2]) == 0):
            actualTimeInSeconds += int(getTime[3:])
        else:
            actualTimeInSeconds += int(getTime[2:])
        #For the exact positioning you have to rewind it first, then set the position.
        pygame.mixer.music.rewind()
        x = -15 if sender1.text() == "15sB" else 15
        #Let's say you are 10 seconds in playing the music and you want to get it 15 backwards.Then the music has to be restarted.
        if (actualTimeInSeconds + x) <= 0:
            self.calc.setCountPosition.emit(0)
            pygame.mixer.music.rewind()
        elif (actualTimeInSeconds + x) >= music.__len__(music.getFile()):
            #Let's say you are 20 seconds in for a 25 seconds music and you want to get it 15 forwards.Then the music has to be stopped at 25 seconds.
            self.calc.setCountPosition.emit(music.__len__(music.getFile()))
        else:
            pygame.mixer.music.set_pos(actualTimeInSeconds + x)
            self.calc.setCountPosition.emit(actualTimeInSeconds + x)


    def sButtonClicked(self):
        if self.stopOrContinue == "stop":
            self.calc.stopSignal.emit("stop")
            self.stopOrContinue = "continue"
        elif self.stopOrContinue == "continue":
            self.calc.wCndt.wakeAll()
            self.calc.continueToSend = True
            self.stopOrContinue = "stop"
        else:
            print("There has been an unexpected error.")
            sys.exit(qApp.exec_())


    def progressButtonClicked(self, music):
        self.calc = ProgressBar()
        self.calc.countChanged.connect(self.changeThePbarValue)
        self.calc.musicLengthSignal.emit(music.__len__(music.getFile()))
        self.pBar.setMaximum(music.__len__(music.getFile()))
        self.durationMusicLabel.setText(self.calculateTheDuration(music,music.getFile()))
        self.calc.moveToTheNextMusic.connect(self.moveNextMusic)
        self.calc.start()

    def changeThePbarValue(self,value):
        valueTuple = divmod(value, 60)
        #I want to time it like 0:02 instead of 0:2 so i've decided to use this format for it.
        actualTime = str(valueTuple[0]) + ":" + "{0:0=2d}".format(valueTuple[1])
        self.timeLabel.setText(actualTime)
        self.pBar.setValue(value)

    def addMusic(self):
        self.msg1 = QMessageBox()
        self.msg1.setIcon(QMessageBox.Information)
        self.msg1.setWindowTitle('Please..')
        self.msg1.setText(
            'There is a restrict on which files can you upload to the application.\nPlease spare time to read details.')
        self.msg1.setDetailedText(
            "You can only upload files like this:\n'My Way-Frank Sinatra-Jazz'\nMeaning:\n1st:Song"
            "\n2nd:Singer\n3rd:Kind\nAnd it has to be .mp3")
        self.msg1.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msg1.buttonClicked.connect(self.addTheFile)
        self.msg1.exec_()

    def addTheFile(self, i):  # i=Which button has been clicked
        if i.text() == "OK":
            self.msg1.close()
            file_name = QFileDialog.getOpenFileName(self, "Open The File", os.getenv(
                "HOME"))  # This will return tuple first element contains the file
            actual_file = file_name[0].split("/")
            a_data = actual_file[-1].split(
                "-")  # The reason for the actual_file[-1] to get the last element hence the actual file we want to upload.
            if len(a_data) != 3 or a_data[-1].endswith(
                    '.mp3') == False:  # Wrong Format to Load a File so program will shut down.
                self.popupError("You have loaded a file that does not fit in to our requirements.")
                return
            else:
                query = "SELECT m_id FROM musics m ORDER BY m_id DESC LIMIT 1"  # What i am doing here is,i am selecting the last row of my table.
                self.mycursor.execute(query)
                temp = self.mycursor.fetchone()

                query2 = "INSERT INTO musics(m_id,m_group,m_name,m_kind,file) VALUES (%s,%s,%s,%s,%s)"
                data2 = (temp[0] + 1, a_data[1], a_data[0], a_data[-1].strip('.mp3'), file_name[0])
                try:
                    self.mycursor.execute(query2, data2)
                    self.mydb.commit()
                except mysql.connector.Error as err:
                    self.popupError(err)
                rowPosition = self.table1.rowCount()
                self.table1.insertRow(rowPosition)
                self.table1.setItem(rowPosition, 0, QTableWidgetItem(str(temp[0] + 1)))
                self.table1.setItem(rowPosition, 1, QTableWidgetItem(a_data[1]))
                self.table1.setItem(rowPosition, 2, QTableWidgetItem(a_data[0]))
                self.table1.setItem(rowPosition, 3, QTableWidgetItem(a_data[-1].strip('.mp3')))
                if self.r_mode !=0:
                    self.sequence.append(int(temp[0]) + 1)

    def addMImage(self, music):
        file_name2 = QFileDialog.getOpenFileName(self, "Open The File", os.getenv(
            "HOME"))  # This will return tuple first element contains the file
        cRow = self.table1.currentRow()
        txt = self.table1.item(cRow, 0)
        t = txt.text()
        try:
            query = "UPDATE musics m SET m.image=%s WHERE m.m_id=%s"
            data = (file_name2[0], t)
            self.mycursor.execute(query, data)
            self.mydb.commit()
        except mysql.connector.Error as err:
            print(err)
        music.setImage(file_name2[0])
        self.volumeAndInfo(music)
        self.update()

    def makeConnection(self):
        dbCredits = []
        with open('dB-Connection.txt', 'r', encoding='utf-8') as database_credentials:
            lines = database_credentials.readlines()
            for line in lines:
                dbCredits.append(line.strip('\n').split(':')[1])

        self.mydb = mysql.connector.connect(
            user=dbCredits[0], password=dbCredits[1],
            host=dbCredits[2], database=dbCredits[3]
        )
        self.mycursor = self.mydb.cursor()

    def exitTheProgram(self):
        sys.exit(qApp.exec_())

    def theChosenFile(self, music):
        self.table1.cellClicked.connect(lambda: self.clickToChooseMusic(music))

    def clickToChooseMusic(self, music):
        self.prevMusic = music.getNameOfTheSong()
        row = self.table1.currentRow()
        if row == 0:  # To make sure when we click one of the topics,program wont shut down.
            return
        txt = self.table1.item(row, 0)
        t = txt.text()
        data = (t,)
        m_data = self.fetchMusicData(data)
        self.setMusicInfos(music, m_data)

    def fetchData(self, music):
        query = "SELECT * FROM musics"
        self.mycursor.execute(query)
        temp2 = self.mycursor.fetchall()
        i = 1  # For rows
        for x in temp2:
            self.table1.setItem(i, 0, QTableWidgetItem(str(x[0])))
            self.table1.setItem(i, 1, QTableWidgetItem(x[1]))
            self.table1.setItem(i, 2, QTableWidgetItem(x[2]))
            self.table1.setItem(i, 3, QTableWidgetItem(x[3]))
            i += 1
        self.clickToChooseMusic(music)

    def createTable(self):
        self.makeConnection()
        self.table1 = QTableWidget()
        temp = self.checkCount()
        self.table1.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table1.horizontalHeader().hide()
        self.table1.verticalHeader().hide()
        a = int(temp[0])
        self.table1.setRowCount(a + 1)  # +1 for captions
        self.table1.setColumnCount(4)
        self.table1.setItem(0, 0, QTableWidgetItem('ID'))
        self.table1.setItem(0, 1, QTableWidgetItem('SINGER/GROUP'))
        self.table1.setItem(0, 2, QTableWidgetItem('MUSIC NAME'))
        self.table1.setItem(0, 3, QTableWidgetItem('MUSIC KIND'))
        if a > 0:
            self.table1.setCurrentCell(1, 0)

    def howToUt(self):
        webbrowser.open('https://github.com/yeKo09/Mp3PlayerPython')

    def clickToPlayMusic(self, music):
        sender = self.sender()
        if sender.text() == "Play":
            if music.getBusy() == 0:
                self.buton.setIcon(
                    QtGui.QIcon('C:\\Users\\yekta\\PycharmProjects\\music_player_python\\icons\\pause.png'))
                #If you click Play button while a music is already playing, the progress bar should be set to 0 again.
                if music.getSOP() == 1:
                    if self.calc.isRunning():
                        self.calc.stop()
                self.progressButtonClicked(music)
                self.stopOrContinue = "stop"
            elif music.getSOP() == 1:  # If music is ready to play,the icon must be play icon
                self.buton.setIcon(
                    QtGui.QIcon('C:\\Users\\yekta\\PycharmProjects\\music_player_python\\icons\\play_icon.png'))
                self.sButtonClicked()
            elif music.getSOP() == 0:  # If music is playing,when you press this button it will pause the music.So icon must be pause icon.
                self.buton.setIcon(
                    QtGui.QIcon('C:\\Users\\yekta\\PycharmProjects\\music_player_python\\icons\\pause.png'))
                self.sButtonClicked()
            music.playTheMusic()
        elif sender.text() == "Previous":
            if self.r_mode != 0:
                if self.index > 0:
                    self.index -= 1
                    data1 = self.sequence[self.index]
                    self.table1.setCurrentCell(data1, 0)
                    self.clickToChooseMusic(music)
                    music.playTheMusic()

                else:
                    pygame.mixer.music.rewind()  # There is no going backwards.So,rewind the music.
            else:
                cRow1 = self.table1.currentRow()
                if cRow1 == 1:  # There is no way down.
                    pygame.mixer.music.rewind()
                else:
                    self.table1.setCurrentCell(cRow1 - 1, 0)
                    self.clickToChooseMusic(music)
                    music.playTheMusic()


            if self.calc.isRunning():
                self.calc.stop()
                self.progressButtonClicked(music)
            else:
                self.progressButtonClicked(music)


        elif sender.text() == "Next":
            if self.r_mode != 0:  # It means we are on the random mode.
                self.index += 1
                if self.index == len(
                        self.sequence):  # If it reaches the end of our playlist,we will initiate reshuffle.
                    self.r_mode = 0
                    self.random_mode(music)
                else:  # Else,we will continue with the random mode using next button.
                    data1 = self.sequence[self.index]
                    self.table1.setCurrentCell(data1, 0)
                    self.clickToChooseMusic(music)
                    music.playTheMusic()

            else:
                cRow = self.table1.currentRow()
                if cRow + 1 >= self.table1.rowCount():  # You cannot go further.
                    pygame.mixer.music.rewind()
                else:
                    self.table1.setCurrentCell(cRow + 1, 0)
                    self.clickToChooseMusic(music)
                    music.playTheMusic()


            if self.calc.isRunning():
                self.calc.stop()
                self.progressButtonClicked(music)
            else:
                self.progressButtonClicked(music)

        elif sender.text() == "Delete":
            tempMusic = self.prevMusic  # I need to get the data of the current music playing.
            checker = self.table1.currentRow()
            query = "DELETE FROM musics m WHERE m.m_id=%s"
            txt = self.table1.item(checker, 0)
            data = (txt.text(),)
            try:
                self.mycursor.execute(query, data)
                self.mydb.commit()
            except mysql.connector.Error as err:
                self.popupError(err)
                sys.exit(qApp.exec_())
            self.etiket2.setText("You have just deleted a music.")
            self.etiket3.setText('')
            self.table1.removeRow(checker)
            # If we are in the random mode,i must remove that element so that we can continue properly.
            if self.r_mode != 0:
                if checker in self.sequence:
                    self.sequence.remove(checker)
                    self.buton2.click()
            else:
                """
                What i am doing with the while loop is that:
                -I have stored the current playing music inside tempMusic
                -And i am comparing it with the tables elements so that if i can find it i can play the current music even i after delete a music
                """
                i = 1
                while i < self.table1.rowCount():
                    if tempMusic == self.table1.item(i, 2).text():
                        self.table1.setCurrentCell(i, 0)
                        self.clickToChooseMusic(music)
                        music.setBusy(1)
                        break
                    i += 1
            return  # Just so that the line below won't be executed.
        self.volumeAndInfo(music)

    def volumeAndInfo(self, music):
        self.sp1.valueChanged.connect(
            lambda: self.valueChange(music))  # If user wants to either increase or decrease the volume of the music.
        self.etiket2.setText(music.__str__())  # Info about the music playing.
        time_place = self.calculateTheDuration(music, music.getFile())  # Duration of the music playing.
        self.etiket3.setText("(" + str(time_place) + ")")
        path = QtGui.QPixmap(music.getImage())
        pixmap = path.scaled(128, 148)
        self.etiket5.setPixmap(pixmap)

    def moveNextMusic(self, mnVal):
        print(mnVal)
        if mnVal == 1337:
            self.nextSong()


    def nextSong(self):
        # If we are on the random mode and if we are not in the last sequence of our random playlist.We have to queue the next music.
        if ((self.table1.currentRow() < self.table1.rowCount()-1 and self.r_mode == 0) or (self.r_mode != 0 and self.index < len(self.sequence) - 1)):
            self.buton2.click()

    def random_mode(self, music):
        temp = self.checkCount()
        self.index = 0
        if self.r_mode == 0:
            self.buton5.setText('Random Mode:E')  # E = Enabled
            self.buton5.setIcon(
                QtGui.QIcon('C:\\Users\\yekta\\PycharmProjects\\music_player_python\\icons\\shuffle.png'))
            self.r_mode = 1
            self.sequence = list()
            while len(self.sequence) != temp[0]:
                r_no = random.randint(1, temp[0])
                if r_no in self.sequence:
                    continue
                else:
                    self.sequence.append(r_no)
            data = self.sequence[self.index]
            if music.getSOP() == 1:
                print('ghello')
                if self.calc.isRunning():
                    self.calc.terminate()
            self.table1.setCurrentCell(data, 0)
            self.clickToChooseMusic(music)
            music.playTheMusic()
            self.volumeAndInfo(music)
            self.progressButtonClicked(music)
        else:
            self.buton5.setText('Random Mode')
            self.buton5.setIcon(
                QtGui.QIcon('C:\\Users\\yekta\\PycharmProjects\\music_player_python\\icons\\random.png'))
            self.r_mode = 0


    def fetchMusicData(self, data):
        query = "SELECT * FROM musics m WHERE m.m_id=%s"
        self.mycursor.execute(query, data)
        temp2 = self.mycursor.fetchone()
        return temp2

    def setMusicInfos(self, music, temp):
        music.setSinger(temp[1])
        music.setNameOfTheSong(temp[2])
        music.setKind(temp[3])
        music.setFile(temp[4])
        music.setImage(temp[5])
        music.setBusy(0)

    def checkCount(self):
        query = "SELECT COUNT(*) FROM musics"
        self.mycursor.execute(query)
        temp = self.mycursor.fetchone()
        return temp

    def popupError(self, err="You cannot make that operation"):
        msg = QMessageBox()
        msg.setWindowTitle('An Unexpected Error Occured')
        msg.setText(err)
        msg.setWindowTitle("Warning")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()

    def calculateTheDuration(self, music, file):
        time_place_hour = (music.__len__(file)) // 60
        time_place_minute = (music.__len__(file)) % 60
        time_place = str(time_place_hour) + ":" + str(time_place_minute)
        return time_place

    def valueChange(self, music):
        music.setVolume(self.sp1.value() / 100)
        pygame.mixer.music.set_volume(music.getVolume())
