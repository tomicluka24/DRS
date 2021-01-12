from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPixmap, QGuiApplication
#from time import sleep
#from random import randint
#from threading import Thread
from time import sleep
import random

i = 0




class Player(QLabel):
    def __init__(self, name, mapa,a,b):
        super().__init__()

        self.player_name = name
        self.player_speed = 1
        self.gravity = 3
        self.player_position = ()
        self.mapa = mapa
        self.a = a
        self.b = b
        self.trenutno = a
        self.canJump = True
        self.canDown = True
        self.zivoti = 3

    def moveRight(self):
        if (self.canJump == False):
            print("Can't move while jumping")
        else:
            if self.mapa.board[self.player_position[0]][self.player_position[1] + 1] == 0:
                print("CAN'T MOVE, WALL")
            elif self.mapa.board[self.player_position[0]][self.player_position[1] + 1] == 1:
                print("Igrac jedan->desno")
                self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                self.mapa.board[self.player_position[0]][self.player_position[1] + 1] = self.a
                self.player_position = (self.player_position[0], self.player_position[1] + 1)
                self.trenutno = self.a
                while (True):
                    # ako smo na bloku iznad cigle, cigle sa zivotima prestani padati
                    if (self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 0 or
                            self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 6 or
                            self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 7 or
                            self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 3 or
                            self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 2 or
                            self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 4 or
                            self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 5):
                        self.canJump = True
                        break
                    else:
                        self.canJump = False
                        self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                        self.mapa.board[self.player_position[0] + 1][self.player_position[1]] = self.trenutno
                        self.player_position = (self.player_position[0] + 1, self.player_position[1])
                        sleep(0.025)

    def moveLeft(self):
        if (self.canJump == False):
            print("Can't move while jumping")
        else:
            if self.mapa.board[self.player_position[0]][self.player_position[1] + -1] == 0:
                print("CAN'T MOVE, WALL")
            elif self.mapa.board[self.player_position[0]][self.player_position[1] - 1] == 1:
                print("Igrac jedan->levo")
                self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                self.mapa.board[self.player_position[0]][self.player_position[1] - 1] = self.b
                self.player_position = (self.player_position[0], self.player_position[1] - 1)
                self.trenutno = self.b
                while (True):
                    # ako smo na bloku iznad cigle, cigle sa zivotima prestani padati
                    if (self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 0 or
                            self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 6 or
                            self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 7 or
                            self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 3 or
                            self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 2 or
                            self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 4 or
                            self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 5):
                        self.canJump = True
                        break
                    else:
                        self.canJump = False
                        self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                        self.mapa.board[self.player_position[0] + 1][self.player_position[1]] = self.trenutno
                        self.player_position = (self.player_position[0] + 1, self.player_position[1])
                        sleep(0.025)

    def jump(self):
        if self.canJump == False:
            print("CAN'T JUMP, JUMPING")

        else:
            self.canJump = False
            # trenutno na prorezu, svakim skokom se pomera gore za jedno a gde bio crta crno jer je prorez
            if (self.player_position[1] == 2 or self.player_position[1] == 3 or self.player_position[1] == 12 or
                    self.player_position[1] == 13):
                for i in range(3):
                    print("UP")
                    self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                    self.mapa.board[self.player_position[0] - 1][self.player_position[1]] = self.trenutno
                    self.player_position = (self.player_position[0] - 1, self.player_position[1])
                    sleep(0.025)
                    self.canJump = True
                # zavrsen skok, graviti?
                while (True):
                    # ako smo na bloku iznad cigle, cigle sa zivotima prestani padati
                    if (self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 0 or
                            self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 6 or
                            self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 7 or
                            self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 3 or
                            self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 2 or
                            self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 4 or
                            self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 5):
                        self.canJump = True
                        break
                    else:
                        self.canJump = False
                        self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                        self.mapa.board[self.player_position[0] + 1][self.player_position[1]] = self.trenutno
                        self.player_position = (self.player_position[0] + 1, self.player_position[1])
                        sleep(0.025)

            else:
                # nije na prorezu
                for i in range(3):
                    print("UP")
                    if (i == 2):
                        # ako je poslednji pomeraj u skoku a x koordinata je 3, onda smo skocili sa najviseg
                        # nivoa i svakim pomerajom(i poslednjim, i==2) iscrtavaj crno na staru poziciju
                        # jer tu nema zidova izmedju pocetka skoka i zavrsetka
                        if (self.player_position[0] == 3):
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                            self.mapa.board[self.player_position[0] - 1][self.player_position[1]] = self.trenutno
                            self.player_position = (self.player_position[0] - 1, self.player_position[1])
                            sleep(0.025)
                        else:
                            # ako je poslednji pomeraj u skoku ali x nije 3, onda nismo skocili sa najviseg nivo sto znaci
                            # da nam je igrac trenutno iscrtan na mestu gde treba biti cigla, jer nismo u prorezu
                            # pa iscrtaj na staro mesto ciglu
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 0
                            self.mapa.board[self.player_position[0] - 1][self.player_position[1]] = self.trenutno
                            self.player_position = (self.player_position[0] - 1, self.player_position[1])
                            sleep(0.025)
                    else:
                        # ako nije poslednji pomeraj u skoku, nisamo na poziciji na kojoj treba biti cigla, pa
                        # mozes da iscrtas crno
                        self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                        self.mapa.board[self.player_position[0] - 1][self.player_position[1]] = self.trenutno
                        self.player_position = (self.player_position[0] - 1, self.player_position[1])
                        sleep(0.025)
                # skok zavrsen, gravity?
                while (True):
                    # ako smo na bloku iznad cigle, cigle sa zivotima prestani padati
                    if (self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 0 or
                            self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 6 or
                            self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 7 or
                            self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 3 or
                            self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 2 or
                            self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 4 or
                            self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 5):
                        self.canJump = True
                        break
                    else:
                        self.canJump = False
                        self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                        self.mapa.board[self.player_position[0] + 1][self.player_position[1]] = self.trenutno
                        self.player_position = (self.player_position[0] + 1, self.player_position[1])
                        sleep(0.025)
            self.canJump = True



    def getCurrentPosition(self):
        return self.player_position

'''
    def moveDown(self):
        #Prvo gledam da li je na onim zivotima ako jeste ne moze dole
        if (
                #self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 0 or
                self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 6 or
                self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 7 or
                self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 3 or
                self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 2 or
                self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 4 or
                self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 5):
                print("CAN'T MOVE, WALL")
                self.canDown=False
        #Ako se nalazi na prvoj liniji a to je 14 pozicija onda isto ne moze dole jer je zid
        elif(self.player_position[0] == 14 or self.player_position[0] == 13 or self.player_position[0] == 12):
            print("Ne moze Dole")
            self.canDown=False
        #ako nije ni jedan od pre ispunjen moze dole
        elif self.canDown==True:
            #ide poziciju po poziciju i spusta se
            for i in range(3):
                print("DOWN")
                #kada prvi put pada stavlja sebe na poziciju cigle i onda se brise cigla
                if(i==0):
                    self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                    self.mapa.board[self.player_position[0] + 1][self.player_position[1]] = self.trenutno
                    self.player_position = (self.player_position[0] + 1, self.player_position[1])
                    sleep(0.025)
                #kada drugi put pada ide jednu poziciju dole i iznad sebe printa ciglu
                else:
                    if(i==1):
                        self.mapa.board[self.player_position[0]][self.player_position[1]] = 0
                        self.mapa.board[self.player_position[0] + 1][self.player_position[1]] = self.trenutno
                        self.player_position = (self.player_position[0] + 1, self.player_position[1])
                        sleep(0.025)
                    #kad nije nista od toga onda samo ide dole i sebe iscrtava
                    else:
                        self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                        self.mapa.board[self.player_position[0] + 1][self.player_position[1]] = self.trenutno
                        self.player_position = (self.player_position[0] + 1, self.player_position[1])
                        sleep(0.025)


        self.canDown = True
'''

