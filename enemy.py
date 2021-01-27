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
        self.imun = False

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
                self.trenutno=self.a
                self.aaa()

            elif (self.mapa.board[self.enemy_position[0]][self.enemy_position[1]+1]==2 or self.mapa.board[self.enemy_position[0]][self.enemy_position[1]+1]==3):
                self.mapa.board[self.enemy_position[0]][self.enemy_position[1]] = 1
                self.mapa.board[self.enemy_position[0]][self.enemy_position[1] + 1] = self.a
                self.enemy_position = (self.enemy_position[0], self.enemy_position[1] + 1)
                self.trenutno = self.a
                self.killplayerone(self.enemy_position[0],self.enemy_position[1]+1)

            elif (self.mapa.board[self.enemy_position[0]][self.enemy_position[1]+1]==4 or self.mapa.board[self.enemy_position[0]][self.enemy_position[1]+1]==5):
                self.mapa.board[self.enemy_position[0]][self.enemy_position[1]] = 1
                self.mapa.board[self.enemy_position[0]][self.enemy_position[1] + 1] = self.a
                self.enemy_position = (self.enemy_position[0], self.enemy_position[1] + 1)
                self.trenutno = self.a
                self.killplayertwo(self.enemy_position[0],self.enemy_position[1]+1)

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
                self.trenutno=self.b
                self.aaa()
            elif (self.mapa.board[self.enemy_position[0]][self.enemy_position[1]-1]==2 or self.mapa.board[self.enemy_position[0]][self.enemy_position[1]-1]==3):
                self.mapa.board[self.enemy_position[0]][self.enemy_position[1]] = 1
                self.mapa.board[self.enemy_position[0]][self.enemy_position[1] - 1] = self.b
                self.enemy_position = (self.enemy_position[0], self.enemy_position[1] - 1)
                self.trenutno = self.b
                self.killplayerone(self.enemy_position[0],self.enemy_position[1]-1)
            elif (self.mapa.board[self.enemy_position[0]][self.enemy_position[1]-1]==2 or self.mapa.board[self.enemy_position[0]][self.enemy_position[1]-1]==3):
                self.mapa.board[self.enemy_position[0]][self.enemy_position[1]] = 1
                self.mapa.board[self.enemy_position[0]][self.enemy_position[1] - 1] = self.b
                self.enemy_position = (self.enemy_position[0], self.enemy_position[1] - 1)
                self.trenutno = self.b
                self.killplayertwo(self.enemy_position[0],self.enemy_position[1]-1)
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
                """
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
                """
                self.aaa()

            else:
                # nije na prorezu
                for i in range(3):

                    print("UP")
                    if (self.mapa.board[self.enemy_position[0] - 1][self.enemy_position[1]] == 10 or self.mapa.board[self.enemy_position[0] - 1][self.enemy_position[1]] == 11):
                        break
                    elif (self.mapa.board[self.enemy_position[0] - 1][self.enemy_position[1]] == 12 or
                          self.mapa.board[self.enemy_position[0] - 1][self.enemy_position[1]] == 13 or
                          self.mapa.board[self.enemy_position[0] - 1][self.enemy_position[1]] == 14 or
                          self.mapa.board[self.enemy_position[0] - 1][self.enemy_position[1]] == 15):
                        print("ENEMY UHVATIO ZAROBLJENOG NEPRIJATELJA $$$")
                        # ako je iznad nas uhvaceni neprijatelj, a mi trenutno na poziciji gde treba biti cigla(redovi 6,9,12) crtaj ciglu
                        # na trenutno mesto, a na mesto iznad igraca i dodaj mu bodove
                        if (self.enemy_position[0] == 6 or self.enemy_position[0] == 9 or self.enemy_position[0] == 12):
                            self.mapa.board[self.enemy_position[0]][self.enemy_position[1]] = 0
                        else:
                            self.mapa.board[self.enemy_position[0]][self.enemy_position[1]] = 1
                        self.mapa.board[self.enemy_position[0] - 1][self.enemy_position[1]] = self.trenutno
                        self.enemy_position = (self.enemy_position[0] - 1, self.enemy_position[1])


                        self.mapa.player1.points=self.mapa.player1.points-10
                        self.mapa.player2.points=self.mapa.player2.points-10

                    elif (self.mapa.board[self.enemy_position[0] - 1][self.enemy_position[1]] == 2 or
                          self.mapa.board[self.enemy_position[0] - 1][self.enemy_position[1]] == 3):

                        if (self.enemy_position[0] == 6 or self.enemy_position[0] == 9 or self.enemy_position[0] == 12):
                            self.mapa.board[self.enemy_position[0]][self.enemy_position[1]] = 0
                        else:
                            self.mapa.board[self.enemy_position[0]][self.enemy_position[1]] = 1
                        self.mapa.board[self.enemy_position[0]-1][self.enemy_position[1]] = self.trenutno
                        self.enemy_position = (self.enemy_position[0]-1, self.enemy_position[1])
                        self.killplayerone(self.enemy_position[0]-1, self.enemy_position[1])
                    elif (self.mapa.board[self.enemy_position[0] - 1][self.enemy_position[1]] == 4 or
                          self.mapa.board[self.enemy_position[0] - 1][self.enemy_position[1]] == 5):

                        if (self.enemy_position[0] == 6 or self.enemy_position[0] == 9 or self.enemy_position[0] == 12):
                            self.mapa.board[self.enemy_position[0]][self.enemy_position[1]] = 0
                        else:
                            self.mapa.board[self.enemy_position[0]][self.enemy_position[1]] = 1
                        self.mapa.board[self.enemy_position[0]-1][self.enemy_position[1]] = self.trenutno
                        self.enemy_position = (self.enemy_position[0]-1, self.enemy_position[1])
                        self.killplayertwo(self.enemy_position[0]-1, self.enemy_position[1])


                    else:
                        # ako se iznad ne nalazi enemy(niti zarobljen niti ziv) proveri da li smo na poziciji gde je cigla(6,9,12)
                        # ako je na tom mestu na to mesto crtaj ciglu, ako nije crtaj black
                        if (self.enemy_position[0] == 6 or self.enemy_position[0] == 9 or self.enemy_position[0] == 12):
                            self.mapa.board[self.enemy_position[0]][self.enemy_position[1]] = 0
                        else:
                            self.mapa.board[self.enemy_position[0]][self.enemy_position[1]] = 1
                        self.mapa.board[self.enemy_position[0] - 1][self.enemy_position[1]] = self.trenutno
                        self.enemy_position = (self.enemy_position[0] - 1, self.enemy_position[1])
                        sleep(0.025)

                # skok zavrsen, gravity?
                self.aaa()
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


    def killplayerone(self, i,j):
        self.mapa.player1.zivoti=self.mapa.player1.zivoti-1
        if (self.mapa.player1.zivoti == 2):
            self.mapa.board[15][2] = 0
            #self.mapa.board[i][j] = 1
            self.mapa.player1.player_position = (14, 1)
            # sleep(0.1)
            self.mapa.board[14][1] = 2
        elif (self.mapa.player1.zivoti == 1):
            self.mapa.board[15][1] = 0
            #self.mapa.board[i][j] = 1
            self.mapa.player1.player_position = (14, 1)
            # sleep(0.1)
            self.mapa.board[14][1] = 2
        elif (self.mapa.player1.zivoti == 0):
            self.mapa.board[15][0] = 0
            #self.mapa.board[i][j] = 1
            self.mapa.player1.player_position = (14, 1)
            # sleep(0.1)
            self.mapa.board[14][1] = 2
        else:
            # KOD ZA KRAJ PARTIJE, IGRAC IZGUBIO SVE ZIVOTE
            print("Game over")


    def killplayertwo(self,i,j):
        self.mapa.player2.zivoti=self.mapa.player2.zivoti-1
        if (self.mapa.player2.zivoti == 2):
            self.mapa.board[15][13] = 0
            #self.mapa.board[i][j] = 1
            self.mapa.player2.player_position = (14, 14)
            # sleep(0.1)
            self.mapa.board[14][14] = 5
        elif (self.mapa.player2.zivoti == 1):
            self.mapa.board[15][14] = 0
            #self.mapa.board[i][j] = 1
            self.mapa.player2.player_position = (14, 14)
            # sleep(0.1)
            self.mapa.board[14][14] = 5
        elif (self.mapa.player2.zivoti == 0):
            self.mapa.board[15][15] = 0
            #self.mapa.board[i][j] = 1
            self.mapa.player2.player_position = (14, 14)
            # sleep(0.1)
            self.mapa.board[14][14] = 5
        else:
            # KOD ZA KRAJ PARTIJE, IGRAC IZGUBIO SVE ZIVOTE
            print("Game over")
    def aaa(self):
        while self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] != 0 and self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] != 6 and self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] != 7:
            self.canJump = False
            self.mapa.board[self.enemy_position[0]][self.enemy_position[1]] = 1

            if (self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] == 2 or self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] == 3):
                self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] = self.trenutno
                self.enemy_position = (self.enemy_position[0] + 1, self.enemy_position[1])
                self.killplayerone(self.enemy_position[0], self.enemy_position[1])
            elif (self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] == 4 or self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] == 5):
                self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] = self.trenutno
                self.enemy_position = (self.enemy_position[0] + 1, self.enemy_position[1])
                self.killplayertwo(self.enemy_position[0], self.enemy_position[1])
            else:

                self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] = self.trenutno
                self.enemy_position = (self.enemy_position[0] + 1, self.enemy_position[1])
                print("vraca za 1")
            # time meri u sekundama
            sleep(0.1)
