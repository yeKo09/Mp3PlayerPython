import pygame
from mutagen.mp3 import MP3

class Music:

    def __init__(self, singer="No One", nameOfTheSong="Nothing", kind="No Kind", file="Nothing",image="Nothing"):
        self.__singer = singer
        self.__nameOfTheSong = nameOfTheSong
        self.__volume = 0.2
        self.__kind = kind
        self.__file = file
        self.__image=image
        self.__s_o_p = 0
        self.__busy = 0
        pygame.init()
        pygame.mixer.pre_init(44100, -16, 2, 2048)  # setup mixer to avoid sound lag

    def __str__(self):
        return "Right now you are playing " + self.__nameOfTheSong + " by " + self.__singer

    def __len__(self, song):
        # I must use mutagen module to get the duration(length) of the song
        pygame.mixer.init()
        # pygame.mixer.music.load(song)
        aSong = MP3(song)
        aSong = round(aSong.info.length)
        return aSong

    def getSinger(self):
        return self.__singer

    def setSinger(self, singer):
        self.__singer = singer

    def getNameOfTheSong(self):
        return self.__nameOfTheSong

    def setNameOfTheSong(self, nameOfTheSong):
        self.__nameOfTheSong = nameOfTheSong

    def getVolume(self):
        return self.__volume

    def setVolume(self, volume):
        self.__volume = volume

    def getKind(self):
        return self.__kind

    def setKind(self, kind):
        self.__kind = kind

    def getSOP(self):
        return self.__s_o_p

    def setSOP(self, s_o_p):
        self.__s_o_p = s_o_p

    def getFile(self):
        return self.__file

    def setFile(self, file):
        self.__file = file

    def setBusy(self,busy):
        self.__busy = busy

    def getBusy(self):
        return self.__busy

    def setImage(self,image):
        self.__image=image

    def getImage(self):
        return self.__image

    def playTheMusic(self):
        # s_o_p = Stopped(0) or Playing(1)
        s_o_p = self.getSOP()
        if self.getBusy() == 0:
            self.setSOP(1)
            self.setBusy(1)
            theSong = pygame.mixer.music.load(self.getFile())
            pygame.mixer.music.set_volume(self.getVolume())
            pygame.mixer.music.play()
        elif s_o_p == 0 and self.getBusy() != 0:
            self.setSOP(1)
            pygame.mixer.music.unpause()
        elif s_o_p == 1:
            pygame.mixer.music.pause()
            self.setSOP(0)
        else:
            print('Incorrect data')