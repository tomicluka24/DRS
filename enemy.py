from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPixmap, QGuiApplication
#from time import sleep
#from enemy import Enemy
#from random import randint
#from threading import Thread
from time import sleep
from threading import Thread
import random


class Enemy(QLabel):
    def __init__(self, name, mapa, a, b):
        super().__init__()

        self.name = name
        self.enemy_speed = 1
        self.gravity = 3
        self.enemy_position = ()
        self.mapa = mapa
        self.a = a
        self.b = b
        self.trenutno = a
        self.alive = True
        self.canJump = True
        self.canDown = True

    def enemy_move_right(self):
        if self.alive == False:
            print('mrtav je ne moze da se pomera')
        if (self.canJump == False):
            print("Can't move while jumping")
        else:
            if self.mapa.board[self.enemy_position[0]][self.enemy_position[1] + 1] == 0:
                print("Protivnik ne moze desno")
            elif self.mapa.board[self.enemy_position[0]][self.enemy_position[1] + 1] == 1:
                print("Igrac jedan->desno")
                self.mapa.board[self.enemy_position[0]][self.enemy_position[1]] = 1
                self.mapa.board[self.enemy_position[0]][self.enemy_position[1] + 1] = self.a
                self.enemy_position = (self.enemy_position[0], self.enemy_position[1] + 1)
                while self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] == 1:
                    self.canJump = False
                    self.mapa.board[self.enemy_position[0]][self.enemy_position[1]] = 1
                    self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] = self.b
                    self.enemy_position = (self.enemy_position[0] + 1, self.enemy_position[1])
                    print("vraca za 1")
                    # time meri u sekundama
                    sleep(0.1)
            self.canJump = True

    def enemy_move_left(self):
        if self.alive == False:
            print('mrtav je ne moze da se pomera')
        if (self.canJump == False):
            print("Can't move while jumping")
        else:
            if self.mapa.board[self.enemy_position[0]][self.enemy_position[1] + -1] == 0:
                print("Protivnik ne moze levo")
            elif self.mapa.board[self.enemy_position[0]][self.enemy_position[1] - 1] == 1:
                print("Igrac jedan->levo")
                self.mapa.board[self.enemy_position[0]][self.enemy_position[1]] = 1
                self.mapa.board[self.enemy_position[0]][self.enemy_position[1] + -1] = self.b
                self.enemy_position = (self.enemy_position[0], self.enemy_position[1] - 1)
                while self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] == 1:
                    self.canJump = False
                    self.mapa.board[self.enemy_position[0]][self.enemy_position[1]] = 1
                    self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] = self.b
                    self.enemy_position = (self.enemy_position[0] + 1, self.enemy_position[1])
                    print("vraca za 1")
                    sleep(0.1)
            self.canJump = True

    def enemy_jump(self):
        if self.alive == False:
            print('mrtav je ne moze da se pomera')
        if self.canJump == False:
            print("Protivnik ne moze gore")
        else:
            self.canJump = False
            # trenutno na prorezu, svakim skokom se pomera gore za jedno a gde bio crta crno jer je prorez
            if (self.enemy_position[1] == 2 or self.enemy_position[1] == 3 or self.enemy_position[1] == 12 or
                    self.enemy_position[1] == 13):
                for i in range(3):
                    print("UP")
                    self.mapa.board[self.enemy_position[0]][self.enemy_position[1]] = 1
                    self.mapa.board[self.enemy_position[0] - 1][self.enemy_position[1]] = self.trenutno
                    self.enemy_position = (self.enemy_position[0] - 1, self.enemy_position[1])
                    sleep(0.025)
                    self.canJump = True
                # zavrsen skok, graviti?
                while (True):
                    # ako smo na bloku iznad cigle, cigle sa zivotima prestani padati
                    if (self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] == 0 or
                            self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] == 6 or
                            self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] == 7 or
                            self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] == 3 or
                            self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] == 2 or
                            self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] == 4 or
                            self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] == 5):
                        self.canJump = True
                        break
                    else:
                        self.canJump = False
                        self.mapa.board[self.enemy_position[0]][self.enemy_position[1]] = 1
                        self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] = self.trenutno
                        self.enemy_position = (self.enemy_position[0] + 1, self.enemy_position[1])
                        sleep(0.025)

            else:
                # nije na prorezu
                for i in range(3):
                    print("UP")
                    if (i == 2):
                        # ako je poslednji pomeraj u skoku a x koordinata je 3, onda smo skocili sa najviseg
                        # nivoa i svakim pomerajom(i poslednjim, i==2) iscrtavaj crno na staru poziciju
                        # jer tu nema zidova izmedju pocetka skoka i zavrsetka
                        if (self.enemy_position[0] == 3):
                            self.mapa.board[self.enemy_position[0]][self.enemy_position[1]] = 1
                            self.mapa.board[self.enemy_position[0] - 1][self.enemy_position[1]] = self.trenutno
                            self.enemy_position = (self.enemy_position[0] - 1, self.enemy_position[1])
                            sleep(0.025)
                        else:
                            # ako je poslednji pomeraj u skoku ali x nije 3, onda nismo skocili sa najviseg nivo sto znaci
                            # da nam je igrac trenutno iscrtan na mestu gde treba biti cigla, jer nismo u prorezu
                            # pa iscrtaj na staro mesto ciglu
                            self.mapa.board[self.enemy_position[0]][self.enemy_position[1]] = 0
                            self.mapa.board[self.enemy_position[0] - 1][self.enemy_position[1]] = self.trenutno
                            self.enemy_position = (self.enemy_position[0] - 1, self.enemy_position[1])
                            sleep(0.025)
                    else:
                        # ako nije poslednji pomeraj u skoku, nisamo na poziciji na kojoj treba biti cigla, pa
                        # mozes da iscrtas crno
                        self.mapa.board[self.enemy_position[0]][self.enemy_position[1]] = 1
                        self.mapa.board[self.enemy_position[0] - 1][self.enemy_position[1]] = self.trenutno
                        self.enemy_position = (self.enemy_position[0] - 1, self.enemy_position[1])
                        sleep(0.025)
                # skok zavrsen, gravity?
                while (True):
                    # ako smo na bloku iznad cigle, cigle sa zivotima prestani padati
                    if (self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] == 0 or
                            self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] == 6 or
                            self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] == 7 or
                            self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] == 3 or
                            self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] == 2 or
                            self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] == 4 or
                            self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] == 5):
                        self.canJump = True
                        break
                    else:
                        self.canJump = False
                        self.mapa.board[self.enemy_position[0]][self.enemy_position[1]] = 1
                        self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] = self.trenutno
                        self.enemy_position = (self.enemy_position[0] + 1, self.enemy_position[1])
                        sleep(0.025)
            self.canJump = True


    def enemy_killed(self):
        self.alive = False


    def pomeranje(self):
        while(self.alive == True):
            p = random.randrange(3)
            if(p == 0):
                self.enemy_move_right()
                break
            elif(p == 1):
                self.enemy_move_left()
                break
            elif(p == 2):
                self.enemy_jump()
                break
            elif(p == 3):
                self.enemy_move_Down()
                break

