from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPixmap, QGuiApplication
#from time import sleep
#from enemy import Enemy
#from random import randint
#from threading import Thread
from time import sleep
from threading import Thread
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
        self.imun = False
        self.points=0
        self.multiplayer=1
        self.pokupioSilu = False

    def moveRight(self):
        if (self.canJump == False):
            print("Can't move while jumping")
        else:
            if self.mapa.board[self.player_position[0]][self.player_position[1] + 1] == 0:
                print("CAN'T MOVE, WALL")
            elif (self.mapa.board[self.player_position[0]][self.player_position[1] + 1] == 10 or self.mapa.board[self.player_position[0]][self.player_position[1] + 1] == 11):
                print("PLAYER HIT ENEMY WHILE MOVING RIGHT")
                if(self.imun==False):
                    self.zivoti=self.zivoti-1
                    if(self.a==2):
                        if(self.zivoti==2):
                            self.mapa.board[15][2]=0
                            self.mapa.board[self.player_position[0]][self.player_position[1]]=1
                            self.player_position=(14,1)
                            #sleep(0.1)
                            self.mapa.board[14][1]=2
                        elif(self.zivoti==1):
                            self.mapa.board[15][1]=0
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                            self.player_position = (14, 1)
                            # sleep(0.1)
                            self.mapa.board[14][1] = 2
                        elif(self.zivoti==0):
                            self.mapa.board[15][0] = 0
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                            self.player_position = (14, 1)
                            # sleep(0.1)
                            self.mapa.board[14][1] = 2
                        else:
                            #KOD ZA KRAJ PARTIJE, IGRAC IZGUBIO SVE ZIVOTE
                            print("Game over")
                    else:
                        if (self.zivoti == 2):
                            self.mapa.board[15][13] = 0
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                            self.player_position = (14, 14)
                            # sleep(0.1)
                            self.mapa.board[14][14] = 5
                        elif (self.zivoti == 1):
                            self.mapa.board[15][14] = 0
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                            self.player_position = (14, 14)
                            # sleep(0.1)
                            self.mapa.board[14][14] = 5
                        elif (self.zivoti == 0):
                            self.mapa.board[15][15] = 0
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                            self.player_position = (14, 14)
                            # sleep(0.1)
                            self.mapa.board[14][14] = 5
                        else:
                            #KOD ZA KRAJ PARTIJE, IGRAC IZGUBIO SVE ZIVOTE
                            print("Game over")

                print("preostali broj zivota:",self.zivoti)
            elif (self.mapa.board[self.player_position[0]][self.player_position[1] + 1] == 12 or self.mapa.board[self.player_position[0]][self.player_position[1] + 1] == 13 or self.mapa.board[self.player_position[0]][self.player_position[1] + 1] == 14 or self.mapa.board[self.player_position[0]][self.player_position[1] + 1] == 15):
                print("PLAYER UHVATIO NEPRIJATELJA $$$")
                self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                self.mapa.board[self.player_position[0]][self.player_position[1] + 1] = self.a
                self.player_position = (self.player_position[0], self.player_position[1] + 1)
                self.trenutno = self.a
                self.points=self.points+100*self.multiplayer
            elif self.mapa.board[self.player_position[0]][self.player_position[1] + 1] == 1:
                if(self.a==2):
                    print("Igrac jedan->desno")
                else:
                    print("Igrac dva->desno")
                self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                self.mapa.board[self.player_position[0]][self.player_position[1] + 1] = self.a
                self.player_position = (self.player_position[0], self.player_position[1] + 1)
                self.trenutno = self.a
                self.aaa()
            elif self.mapa.board[self.player_position[0]][self.player_position[1] + 1] == 16:
                self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                self.mapa.board[self.player_position[0]][self.player_position[1] + 1] = self.a
                self.player_position = (self.player_position[0], self.player_position[1] + 1)
                self.trenutno = self.a
                self.pokupioSilu = True

    def moveLeft(self):
        if (self.canJump == False):
            print("Can't move while jumping")
        else:
            if self.mapa.board[self.player_position[0]][self.player_position[1] + -1] == 0:
                print("CAN'T MOVE, WALL")
            elif (self.mapa.board[self.player_position[0]][self.player_position[1] - 1] == 10 or self.mapa.board[self.player_position[0]][self.player_position[1] - 1] == 11):
                print("PLAYER HIT ENEMY WHILE MOVING LEFT")
                if (self.imun == False):
                    self.zivoti = self.zivoti - 1
                    if (self.a == 2):
                        if (self.zivoti == 2):
                            self.mapa.board[15][2] = 0
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                            self.player_position = (14, 1)
                            # sleep(0.1)
                            self.mapa.board[14][1] = 2
                        elif (self.zivoti == 1):
                            self.mapa.board[15][1] = 0
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                            self.player_position = (14, 1)
                            # sleep(0.1)
                            self.mapa.board[14][1] = 2
                        elif (self.zivoti == 0):
                            self.mapa.board[15][0] = 0
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                            self.player_position = (14, 1)
                            # sleep(0.1)
                            self.mapa.board[14][1] = 2
                        else:
                            # KOD ZA KRAJ PARTIJE, IGRAC IZGUBIO SVE ZIVOTE
                            print("Game over")
                    else:
                        if (self.zivoti == 2):
                            self.mapa.board[15][13] = 0
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                            self.player_position = (14, 14)
                            # sleep(0.1)
                            self.mapa.board[14][14] = 5
                        elif (self.zivoti == 1):
                            self.mapa.board[15][14] = 0
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                            self.player_position = (14, 14)
                            # sleep(0.1)
                            self.mapa.board[14][14] = 5
                        elif (self.zivoti == 0):
                            self.mapa.board[15][15] = 0
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                            self.player_position = (14, 14)
                            # sleep(0.1)
                            self.mapa.board[14][14] = 5
                        else:
                            #KOD ZA KRAJ PARTIJE, IGRAC IZGUBIO SVE ZIVOTE
                            print("Game over")

                print("preostali broj zivota:", self.zivoti)
            elif (self.mapa.board[self.player_position[0]][self.player_position[1] - 1] == 12 or self.mapa.board[self.player_position[0]][self.player_position[1] - 1] == 13 or self.mapa.board[self.player_position[0]][self.player_position[1] - 1] == 14 or self.mapa.board[self.player_position[0]][self.player_position[1] - 1] == 15):
                print("PLAYER UHVATIO NEPRIJATELJA $$$")
                self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                self.mapa.board[self.player_position[0]][self.player_position[1] - 1] = self.b
                self.player_position = (self.player_position[0], self.player_position[1] - 1)
                self.trenutno = self.b
                self.points=self.points+100*self.multiplayer

            elif self.mapa.board[self.player_position[0]][self.player_position[1] - 1] == 1:
                if (self.a == 2):
                    print("Igrac jedan->levo")
                else:
                    print("Igrac dva->levo")
                self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                self.mapa.board[self.player_position[0]][self.player_position[1] - 1] = self.b
                self.player_position = (self.player_position[0], self.player_position[1] - 1)
                self.trenutno = self.b
                self.aaa()
            elif self.mapa.board[self.player_position[0]][self.player_position[1] - 1] == 16:
                self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                self.mapa.board[self.player_position[0]][self.player_position[1] - 1] = self.b
                self.player_position = (self.player_position[0], self.player_position[1] - 1)
                self.trenutno = self.b
                self.pokupioSilu = True

    def jump(self):
        if self.canJump == False:
            print("CAN'T JUMP, JUMPING")
        else:
            self.canJump = False
            # trenutno na prorezu, svakim skokom se pomera gore za jedno a gde bio crta crno jer je prorez
            if (self.player_position[1] == 2 or self.player_position[1] == 3 or self.player_position[1] == 12 or self.player_position[1] == 13):
                for i in range(3):

                    print("UP")
                    if (self.mapa.board[self.player_position[0]-1][self.player_position[1]] == 10 or self.mapa.board[self.player_position[0]-1][self.player_position[1]] == 11):
                        print("PLAYER HIT ENEMY WHILE JUMPING")
                        if (self.imun == False):
                            self.zivoti = self.zivoti - 1
                            if (self.a == 2):
                                if (self.zivoti == 2):
                                    self.mapa.board[15][2] = 0
                                    self.mapa.board[self.player_position[0]][self.player_position[1]] = 1

                                    self.player_position = (14, 1)
                                    # sleep(0.1)
                                    self.mapa.board[14][1] = 2
                                    self.canJump=True
                                    break
                                elif (self.zivoti == 1):
                                    self.mapa.board[15][1] = 0
                                    self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                                    self.player_position = (14, 1)
                                    # sleep(0.1)
                                    self.mapa.board[14][1] = 2
                                    self.canJump = True
                                    break
                                elif (self.zivoti == 0):
                                    self.mapa.board[15][0] = 0
                                    self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                                    self.player_position = (14, 1)
                                    # sleep(0.1)
                                    self.mapa.board[14][1] = 2
                                    self.canJump = True
                                    break
                                else:
                                    # KOD ZA KRAJ PARTIJE, IGRAC IZGUBIO SVE ZIVOTE

                                    print("Game over")
                            else:
                                if (self.zivoti == 2):
                                    self.mapa.board[15][13] = 0
                                    self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                                    self.player_position = (14, 14)
                                    # sleep(0.1)
                                    self.mapa.board[14][14] = 5
                                    self.canJump = True
                                    break
                                elif (self.zivoti == 1):
                                    self.mapa.board[15][14] = 0
                                    self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                                    self.player_position = (14, 14)
                                    # sleep(0.1)
                                    self.mapa.board[14][14] = 5
                                    self.canJump = True
                                    break
                                elif (self.zivoti == 0):
                                    self.mapa.board[15][15] = 0
                                    self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                                    self.player_position = (14, 14)
                                    # sleep(0.1)
                                    self.mapa.board[14][14] = 5
                                    self.canJump = True
                                    break
                                else:
                                    # KOD ZA KRAJ PARTIJE, IGRAC IZGUBIO SVE ZIVOTE
                                    print("Game over")

                        print("preostali broj zivota:", self.zivoti)

                        self.canJump = True
                        self.aaa()
                    elif(self.mapa.board[self.player_position[0]-1][self.player_position[1]] == 2 or self.mapa.board[self.player_position[0]-1][self.player_position[1]] == 3 or self.mapa.board[self.player_position[0]-1][self.player_position[1]] == 4 or self.mapa.board[self.player_position[0]-1][self.player_position[1]] == 5):
                        break
                    elif (self.mapa.board[self.player_position[0] - 1][self.player_position[1]] == 12 or
                          self.mapa.board[self.player_position[0] - 1][self.player_position[1]] == 13 or
                          self.mapa.board[self.player_position[0] - 1][self.player_position[1]] == 14 or
                          self.mapa.board[self.player_position[0] - 1][self.player_position[1]] == 15):
                        print("PLAYER UHVATIO NEPRIJATELJA $$$")
                        # ako je iznad nas uhvaceni neprijatelj, a mi trenutno na poziciji gde treba biti cigla(redovi 6,9,12) crtaj ciglu
                        # na trenutno mesto, a na mesto iznad igraca i dodaj mu bodove
                        if (self.player_position[0] == 6 or self.player_position[0] == 9 or self.player_position[
                            0] == 12):
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 0
                        else:
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                        self.mapa.board[self.player_position[0] - 1][self.player_position[1]] = self.trenutno
                        self.player_position = (self.player_position[0] - 1, self.player_position[1])

                        self.points = self.points + 100 * self.multiplayer
                    else:
                        self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                        self.mapa.board[self.player_position[0] - 1][self.player_position[1]] = self.trenutno
                        self.player_position = (self.player_position[0] - 1, self.player_position[1])
                        sleep(0.025)

                self.aaa()
            else:
                # nije na prorezu
                 for i in range(3):

                    print("UP")
                    if (self.mapa.board[self.player_position[0]-1][self.player_position[1]] == 10 or self.mapa.board[self.player_position[0]-1][self.player_position[1]] == 11):
                        print("PLAYER HIT ENEMY WHILE JUMPING")
                        if (self.imun == False):
                            self.zivoti = self.zivoti - 1
                            if (self.a == 2):
                                if (self.zivoti == 2):
                                    self.mapa.board[15][2] = 0
                                    if(self.player_position[0]==6 or self.player_position[0]==9 or self.player_position[0]==12):
                                        self.mapa.board[self.player_position[0]][self.player_position[1]] = 0
                                    else:
                                        self.mapa.board[self.player_position[0]][self.player_position[1]] = 1

                                    self.player_position = (14, 1)
                                    # sleep(0.1)
                                    self.mapa.board[14][1] = 2
                                elif (self.zivoti == 1):
                                    self.mapa.board[15][1] = 0
                                    if (self.player_position[0]==6 or self.player_position[0]==9 or self.player_position[0]==12):
                                        self.mapa.board[self.player_position[0]][self.player_position[1]] = 0
                                    else:
                                        self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                                    self.player_position = (14, 1)
                                    # sleep(0.1)
                                    self.mapa.board[14][1] = 2
                                elif (self.zivoti == 0):
                                    self.mapa.board[15][0] = 0
                                    if (self.player_position[0]==6 or self.player_position[0]==9 or self.player_position[0]==12):
                                        self.mapa.board[self.player_position[0]][self.player_position[1]] = 0
                                    else:
                                        self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                                    self.player_position = (14, 1)
                                    # sleep(0.1)
                                    self.mapa.board[14][1] = 2
                                else:
                                    # KOD ZA KRAJ PARTIJE, IGRAC IZGUBIO SVE ZIVOTE

                                    print("Game over")
                            else:
                                if (self.zivoti == 2):
                                    self.mapa.board[15][13] = 0
                                    if (self.player_position[0]==6 or self.player_position[0]==9 or self.player_position[0]==12):
                                        self.mapa.board[self.player_position[0]][self.player_position[1]] = 0
                                    else:
                                        self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                                    self.player_position = (14, 14)
                                    # sleep(0.1)
                                    self.mapa.board[14][14] = 5
                                elif (self.zivoti == 1):
                                    self.mapa.board[15][14] = 0
                                    if (self.player_position[0]==6 or self.player_position[0]==9 or self.player_position[0]==12):
                                        self.mapa.board[self.player_position[0]][self.player_position[1]] = 0
                                    else:
                                        self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                                    self.player_position = (14, 14)
                                    # sleep(0.1)
                                    self.mapa.board[14][14] = 5
                                elif (self.zivoti == 0):
                                    self.mapa.board[15][15] = 0
                                    if (self.player_position[0]==6 or self.player_position[0]==9 or self.player_position[0]==12):
                                        self.mapa.board[self.player_position[0]][self.player_position[1]] = 0
                                    else:
                                        self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                                    self.player_position = (14, 14)
                                    # sleep(0.1)
                                    self.mapa.board[14][14] = 5
                                else:
                                    # KOD ZA KRAJ PARTIJE, IGRAC IZGUBIO SVE ZIVOTE
                                    print("Game over")

                        print("preostali broj zivota:", self.zivoti)
                    elif(self.mapa.board[self.player_position[0]-1][self.player_position[1]] == 12 or self.mapa.board[self.player_position[0]-1][self.player_position[1]] == 13 or self.mapa.board[self.player_position[0]-1][self.player_position[1]] == 14 or self.mapa.board[self.player_position[0]-1][self.player_position[1]] == 15):
                        print("PLAYER UHVATIO NEPRIJATELJA $$$")
                        #ako je iznad nas uhvaceni neprijatelj, a mi trenutno na poziciji gde treba biti cigla(redovi 6,9,12) crtaj ciglu
                        #na trenutno mesto, a na mesto iznad igraca i dodaj mu bodove
                        if ( self.player_position[0]==6 or self.player_position[0]==9 or self.player_position[0]==12):
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 0
                        else:
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                        self.mapa.board[self.player_position[0]-1][self.player_position[1]] = self.trenutno
                        self.player_position = (self.player_position[0]-1, self.player_position[1])

                        self.points = self.points + 100 * self.multiplayer
                    elif (self.mapa.board[self.player_position[0] - 1][self.player_position[1]] == 2 or
                          self.mapa.board[self.player_position[0] - 1][self.player_position[1]] == 3 or
                          self.mapa.board[self.player_position[0] - 1][self.player_position[1]] == 4 or
                          self.mapa.board[self.player_position[0] - 1][self.player_position[1]] == 5):
                        break
                    else:
                            #ako se iznad ne nalazi enemy(niti zarobljen niti ziv) proveri da li smo na poziciji gde je cigla(6,9,12)
                            #ako je na tom mestu na to mesto crtaj ciglu, ako nije crtaj black
                            if (self.mapa.board[self.player_position[0] - 1][self.player_position[1]] == 16):
                                self.mapa.board[self.player_position[0]][self.player_position[1]] = 0
                                self.mapa.board[self.player_position[0] - 1][self.player_position[1]] = self.trenutno
                                self.player_position = (self.player_position[0] - 1, self.player_position[1])
                                self.pokupioSilu = True
                                break
                            elif (self.player_position[0]==6 or self.player_position[0]==9 or self.player_position[0]==12):
                                self.mapa.board[self.player_position[0]][self.player_position[1]] = 0
                            #proveri da li je sila iznad ako jeste crtaj sebe i stavi da je pokipio Silu ako ne


                            else:
                             self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                            self.mapa.board[self.player_position[0] - 1][self.player_position[1]] = self.trenutno
                            self.player_position = (self.player_position[0] - 1, self.player_position[1])
                            sleep(0.025)


                # skok zavrsen, gravity?

            self.aaa()

    def aaa(self):
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
            elif(self.mapa.board[self.player_position[0]+1][self.player_position[1]]==10 or self.mapa.board[self.player_position[0]+1][self.player_position[1]]==11):
                print("DIED WHILE FALLING")
                self.zivoti=self.zivoti-1
                if (self.a == 2):
                    if (self.zivoti == 2):
                        self.mapa.board[15][2] = 0
                        if ((self.player_position[0] == 6 or self.player_position[0] == 9 or self.player_position[0] == 12) and ((self.player_position[1]!=2) and (self.player_position[1]!=3) and (self.player_position[1]!=13) and (self.player_position[1]!=12))):
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 0
                        else:
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 1

                        self.player_position = (14, 1)
                        # sleep(0.1)
                        self.mapa.board[14][1] = 2
                    elif (self.zivoti == 1):
                        self.mapa.board[15][1] = 0
                        if ((self.player_position[0] == 6 or self.player_position[0] == 9 or self.player_position[0] == 12) and ((self.player_position[1]!=2) and (self.player_position[1]!=3) and (self.player_position[1]!=13) and (self.player_position[1]!=12))):
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 0
                        else:
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                        self.player_position = (14, 1)
                        # sleep(0.1)
                        self.mapa.board[14][1] = 2
                    elif (self.zivoti == 0):
                        self.mapa.board[15][0] = 0
                        if ((self.player_position[0] == 6 or self.player_position[0] == 9 or self.player_position[0] == 12) and ((self.player_position[1]!=2) and (self.player_position[1]!=3) and (self.player_position[1]!=13) and (self.player_position[1]!=12))):
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 0
                        else:
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                        self.player_position = (14, 1)
                        # sleep(0.1)
                        self.mapa.board[14][1] = 2
                    else:
                        # KOD ZA KRAJ PARTIJE, IGRAC IZGUBIO SVE ZIVOTE

                        print("Game over")
                else:
                    if (self.zivoti == 2):
                        self.mapa.board[15][13] = 0
                        if ((self.player_position[0] == 6 or self.player_position[0] == 9 or self.player_position[0] == 12) and ((self.player_position[1]!=2) and (self.player_position[1]!=3) and (self.player_position[1]!=13) and (self.player_position[1]!=12))):
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 0
                        else:
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                        self.player_position = (14, 14)
                        # sleep(0.1)
                        self.mapa.board[14][14] = 5
                    elif (self.zivoti == 1):
                        self.mapa.board[15][14] = 0
                        if ((self.player_position[0] == 6 or self.player_position[0] == 9 or self.player_position[0] == 12) and ((self.player_position[1]!=2) and (self.player_position[1]!=3) and (self.player_position[1]!=13) and (self.player_position[1]!=12))):
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 0
                        else:
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                        self.player_position = (14, 14)
                        # sleep(0.1)
                        self.mapa.board[14][14] = 5
                    elif (self.zivoti == 0):
                        self.mapa.board[15][15] = 0
                        if ((self.player_position[0] == 6 or self.player_position[0] == 9 or self.player_position[0] == 12) and ((self.player_position[1]!=2) and (self.player_position[1]!=3) and (self.player_position[1]!=13) and (self.player_position[1]!=12))):
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 0
                        else:
                            self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                        self.player_position = (14, 14)
                        # sleep(0.1)
                        self.mapa.board[14][14] = 5
                    else:
                        # KOD ZA KRAJ PARTIJE, IGRAC IZGUBIO SVE ZIVOTE
                        print("Game over")
            elif (self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 12 or
                  self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 13 or
                  self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 14 or
                  self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 15):
                print("PLAYER UHVATIO NEPRIJATELJA $$$")
                # ako je iznad nas uhvaceni neprijatelj, a mi trenutno na poziciji gde treba biti cigla(redovi 6,9,12) crtaj ciglu
                # na trenutno mesto, a na mesto iznad igraca i dodaj mu bodove
                if ((self.player_position[0] == 6 or self.player_position[0] == 9 or self.player_position[0] == 12) and ((self.player_position[1]!=2) and (self.player_position[1]!=3) and (self.player_position[1]!=13) and (self.player_position[1]!=12))):
                    self.mapa.board[self.player_position[0]][self.player_position[1]] = 0
                else:
                    self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                self.mapa.board[self.player_position[0] + 1][self.player_position[1]] = self.trenutno
                self.player_position = (self.player_position[0] + 1, self.player_position[1])

                self.points = self.points + 100 * self.multiplayer
            else:
                self.canJump = False
                self.mapa.board[self.player_position[0]][self.player_position[1]] = 1
                self.mapa.board[self.player_position[0] + 1][self.player_position[1]] = self.trenutno
                self.player_position = (self.player_position[0] + 1, self.player_position[1])
                sleep(0.025)
        self.canJump = True

    def shoot(self):
        if(self.pokupioSilu == True):
            a=6
        else:
            a=4
        (x, y) = (self.player_position[0], self.player_position[1])
        # igrac.a==2 -> u pitanju je igrac 1->zeleni
        if (self.a == 2):
            # igrac p1 trenutno glededa u desno
            if (self.trenutno == 2):
                for i in range(1, a):
                    # balon na sledecoj poziciji nije naisao ninasta->nacrtaj ga, uspavaj nit pa vrati crno, radi efekta
                    if self.mapa.board[x][y + i] == 1:
                        print(i)
                        self.mapa.board[x][y + i] = 8
                        sleep(0.1)
                        print("Woke up")
                        if (self.mapa.board[x][y + i] == 8):
                            self.mapa.board[x][y + i] = 1
                        print("Set to black")
                    # ako je balon na sledecoj poziciji naisao na neprijatelja koji gleda u desno i zarobi ga
                    elif self.mapa.board[x][y + i] == 10:
                        self.mapa.board[x][y + i] = 12

                        print("UVatio neprijatelja")
                        sleep(15)
                        print("Neprijatelj nestao")
                        # zarobljeni neprijatelj stoji u balonu 15 sek, ako se posle 15 sek ne uhvati nestane
                        if self.mapa.board[x][y + i] == 12:
                            self.mapa.board[x][y + i] = 1
                            break
                        break
                    elif self.mapa.board[x][y + i] == 11:
                        self.mapa.board[x][y + i] = 13
                        print("P1 koji gleda desno uhvatio neprijatelja koji gleda levo")
                        sleep(15)
                        print("Neprijatelj nestao")
                        if self.mapa.board[x][y + i] == 13:
                            self.mapa.board[x][y + i] = 1
                            break
                        break
                    elif self.mapa.board[x][y + i] == 4 or self.mapa.board[x][y + i] == 5 or self.mapa.board[x][
                        y + i] == 0 or self.mapa.board[x][y + i] == 2 or self.mapa.board[x][y + i] == 3 or \
                            self.mapa.board[x][y + i] == 9:  # naisao na prepreku(zid, igraca 2)
                        break
            # ako igrac p1 gleda u levo
            elif (self.trenutno == 3):
                print("gledam u levo")
                for i in range(1, a):
                    if self.mapa.board[x][y - i] == 1:
                        print(i)
                        self.mapa.board[x][y - i] = 8
                        sleep(0.1)
                        print("Woke up")
                        if (self.mapa.board[x][y - i] == 8):
                            self.mapa.board[x][y - i] = 1
                        print("Set to black")
                    # ako je balon na sledecoj poziciji naisao na neprijatelja koji gleda u desno i zarobi ga
                    elif self.mapa.board[x][y - i] == 10:
                        self.mapa.board[x][y - i] = 12
                        print("P1 koji gleda levo uhvatio neprijatelja koji gleda desno")
                        sleep(15)
                        print("Neprijatelj nestao")
                        # zarobljeni neprijatelj stoji u balonu 15 sek, ako se posle 15 sek ne uhvati nestane
                        if self.mapa.board[x][y - i] == 12:
                            self.mapa.board[x][y - i] = 1
                            break
                        break
                    elif self.mapa.board[x][y - i] == 11:
                        self.mapa.board[x][y - i] = 13
                        print("P1 koji gleda levo uhvatio neprijatelja koji gleda levo")
                        sleep(15)
                        print("Neprijatelj nestao")
                        if self.mapa.board[x][y - i] == 13:
                            self.mapa.board[x][y - i] = 1
                            break
                        break

                    elif self.mapa.board[x][y - i] == 4 or self.mapa.board[x][y - i] == 5 or self.mapa.board[x][
                        y - i] == 0 or self.mapa.board[x][y - i] == 2 or self.mapa.board[x][y - i] == 3 or \
                            self.mapa.board[x][y - i] == 9:  # naisao na prepreku(zid, igraca 2, balon protivnika)
                        break
        elif (self.a == 4):
            # igrac p2
            if (self.trenutno == 4):
                # gleda u desno
                for i in range(1, a):
                    if self.mapa.board[x][y + i] == 1:
                        print(i)
                        self.mapa.board[x][y + i] = 9
                        sleep(0.1)
                        print("Woke up")
                        if (self.mapa.board[x][y + i] == 9):
                            self.mapa.board[x][y + i] = 1
                        print("Set to black")
                    elif self.mapa.board[x][y + i] == 10:
                        self.mapa.board[x][y + i] = 14
                        print("P2 uhvation neprijatelja koji gleda u desno ")
                        sleep(15)
                        print("Neprijatelj nestao")
                        # zarobljeni neprijatelj stoji u balonu 15 sek, ako se posle 15 sek ne uhvati nestane
                        if self.mapa.board[x][y + i] == 14:
                            self.mapa.board[x][y + i] = 1
                            break
                        break
                    elif self.mapa.board[x][y + i] == 11:
                        self.mapa.board[x][y + i] = 15
                        print("P2 koji gleda desno uhvatio neprijatelja koji gleda levo")
                        sleep(15)
                        print("Neprijatelj nestao")
                        if self.mapa.board[x][y + i] == 15:
                            self.mapa.board[x][y + i] = 1
                            break
                        break
                    # naisao na prepreku(zid, igraca 2)
                    elif self.mapa.board[x][y + i] == 4 or self.mapa.board[x][y + i] == 5 or self.mapa.board[x][
                        y + i] == 0 or self.mapa.board[x][y + i] == 2 or self.mapa.board[x][y + i] == 3 or \
                            self.mapa.board[x][y + i] == 8:
                        break
            if (self.trenutno == 5):
                for i in range(1, a):
                    if self.mapa.board[x][y - i] == 1:
                        print(i)
                        self.mapa.board[x][y - i] = 9
                        sleep(0.1)
                        print("Woke up")
                        if (self.mapa.board[x][y - i] == 9):
                            self.mapa.board[x][y - i] = 1
                        print("Set to black")
                    elif self.mapa.board[x][y - i] == 10:
                        self.mapa.board[x][y - i] = 14
                        print("P2 uhvation neprijatelja koji gleda u desno ")
                        sleep(15)
                        print("Neprijatelj nestao")
                        # zarobljeni neprijatelj stoji u balonu 15 sek, ako se posle 15 sek ne uhvati nestane
                        if self.mapa.board[x][y - i] == 14:
                            self.mapa.board[x][y - i] = 1
                            break
                        break
                    elif self.mapa.board[x][y - i] == 11:
                        self.mapa.board[x][y - i] = 15
                        print("P2 koji gleda levo uhvatio neprijatelja koji gleda levo")
                        sleep(15)
                        print("Neprijatelj nestao")
                        if self.mapa.board[x][y - i] == 15:
                            self.mapa.board[x][y - i] = 1
                            break
                        break
                    # naisao na prepreku(zid, igraca 2)
                    elif self.mapa.board[x][y - i] == 4 or self.mapa.board[x][y - i] == 5 or self.mapa.board[x][
                        y - i] == 0 or self.mapa.board[x][y - i] == 2 or self.mapa.board[x][y - i] == 3 or \
                            self.mapa.board[x][y - i] == 8:
                        break

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
        #POMERANJE DOLE
'''
    def enemy_move_Down(self):
        #Prvo gledam da li je na onim zivotima ako jeste ne moze dole
        if (
                #self.mapa.board[self.player_position[0] + 1][self.player_position[1]] == 0 or
                self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] == 6 or
                self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] == 7 or
                self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] == 3 or
                self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] == 2 or
                self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] == 4 or
                self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] == 5):
                print("Protivnik ne moze dole")
                self.canDown=False
        #Ako se nalazi na prvoj liniji a to je 14 pozicija onda isto ne moze dole jer je zid
        elif(self.enemy_position[0] == 14 or self.enemy_position[0] == 13 or self.enemy_position[0] == 12):
            print("Protivnik ne moze dole")
            self.canDown=False
        #ako nije ni jedan od pre ispunjen moze dole
        elif self.canDown==True:
            #ide poziciju po poziciju i spusta se
            for i in range(3):
                print("DOWN")
                #kada prvi put pada stavlja sebe na poziciju cigle i onda se brise cigla
                if(i==0):
                    self.mapa.board[self.enemy_position[0]][self.enemy_position[1]] = 1
                    self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] = self.trenutno
                    self.enemy_position = (self.enemy_position[0] + 1, self.enemy_position[1])
                    sleep(0.025)
                #kada drugi put pada ide jednu poziciju dole i iznad sebe printa ciglu
                else:
                    if(i==1):
                        self.mapa.board[self.enemy_position[0]][self.enemy_position[1]] = 0
                        self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] = self.trenutno
                        self.enemy_position = (self.enemy_position[0] + 1, self.enemy_position[1])
                        sleep(0.025)
                    #kad nije nista od toga onda samo ide dole i sebe iscrtava
                    else:
                        self.mapa.board[self.enemy_position[0]][self.enemy_position[1]] = 1
                        self.mapa.board[self.enemy_position[0] + 1][self.enemy_position[1]] = self.trenutno
                        self.enemy_position = (self.enemy_position[0] + 1, self.enemy_position[1])
                        sleep(0.025)
        self.canDown = True
'''
