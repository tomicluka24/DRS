from PyQt5.QtCore import Qt, QThread
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from map import Map
from player import Player
from enemy import Enemy
from key_notifier import KeyNotifier

import time
import random
from threading import *

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

# P1_INIT_ROW = 14
# P1_INIT_COLUMN = 1

# P2_INIT_ROW = 14
# P2_INIT_COLUMN = 14

P1_INIT_POS = (14, 5)
P2_INIT_POS = (14, 14)

brzina = 0

class GameWindow(QMainWindow):
    win_change_signal = QtCore.pyqtSignal()

    def __init__(self, list_of_names):
        super().__init__()

        # p1 = green
        # p2 = blue
        self.brzina = 0
        self.map = Map()
        self.p1 = Player(list_of_names[0], self.map, 2, 3)
        self.p1.player_position = (14, 5)
        self.p2 = Player(list_of_names[1], self.map, 4, 5)
        self.p2.player_position = (14, 14)
        self.e1 = Enemy('benzo', self.map, 10, 11)
        self.e1.enemy_position = (5, 5)
        self.e2 = Enemy('boris', self.map, 10, 11)
        self.e2.enemy_position = (5, 10)
        self.e3 = Enemy(' bonie ', self.map, 10, 11)
        self.e3.enemy_position = (11, 8)
        #self.sila=Sila('sila', self.map, 16)
        self.map.player1=self.p1
        self.map.player2=self.p2

        list = []  # (self.e1,self.e2, self.e3)
        list.append(self.e1)
        list.append(self.e2)
        list.append(self.e3)
        self.map.enemies = list

        self.map.board[5][5] = 10
        self.map.board[5][10] = 10
        self.map.board[11][8] = 10
        self.map.board[14][5] = 2
        self.map.board[14][14] = 5

        self.map.board[15][0] = 6
        self.map.board[15][1] = 6
        self.map.board[15][2] = 6

        self.map.board[15][15] = 7
        self.map.board[15][14] = 7
        self.map.board[15][13] = 7

        self.key_notifier = KeyNotifier()
        self.key_notifier.key_signal.connect(self.__update_position__)
        self.key_notifier.start()

        self.enemyPosition = QThread
        self.enemyPosition = Thread(target=self.__update_enemyPosition__, args=[])
        self.enemyPosition.start()

        self.pojavaSile = QThread
        self.pojavaSile = Thread(target=self.__pojavaSile__, args=[])
        self.pojavaSile.start()

        self.nivo = QThread
        self.nivo = Thread(target=self.__thread_Nivo__, args=[])
        self.nivo.start()


        self.init_ui()

        self.lives = QThread
        self.lives = Thread(target=self.provera, args=[])
        self.lives.start()

        # self.__update_enemyPosition__()



    def init_ui(self):
        self.setWindowTitle('Try to win, if u can :P')
        self.setFixedSize(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.setCentralWidget(self.map)

    def provera(self):
        while(True):
            if(self.p1.zivoti>0 and self.p2.zivoti==0):
                self.player1LastedLonger=True
            if(self.p2.zivoti>0 and self.p1.zivoti==0):
                self.player1LastedLonger=False

            if(self.p1.zivoti==0 and self.p2.zivoti==0):
                print("Oba mrtva")
                self.win_change_signal.emit()
                break

    def keyPressEvent(self, event):
        self.key_notifier.add_key(event.key())

    def __update_position__(self, key):
        if key == Qt.Key_D:
            self.player1_thread = Thread(target=self.p1.moveRight, args=[])
            self.player1_thread.start()
        elif key == Qt.Key_A:
            self.player1_thread = Thread(target=self.p1.moveLeft, args=[])
            self.player1_thread.start()
        elif key == Qt.Key_W:
            self.player1_thread = Thread(target=self.p1.jump, args=[])
            self.player1_thread.start()
        # elif key == Qt.Key_S:
        #    self.player1_thread = Thread(target=self.p1.moveDown, args=[])
        #  self.player1_thread.start()
        elif key == Qt.Key_Space:
            self.player1_thread = Thread(target=self.p1.shoot, args=[])
            self.player1_thread.start()
        if key == Qt.Key_Left:
            self.player2_thread = Thread(target=self.p2.moveLeft, args=[])
            self.player2_thread.start()
        elif key == Qt.Key_Right:
            self.player2_thread = Thread(target=self.p2.moveRight, args=[])
            self.player2_thread.start()
        elif key == Qt.Key_Up:
            self.player2_thread = Thread(target=self.p2.jump, args=[])
            self.player2_thread.start()
        # elif key == Qt.Key_Down:
        #    self.player2_thread = Thread(target=self.p2.moveDown, args=[])
        #   self.player2_thread.start()

        elif key == Qt.Key_0:
            self.player2_thread = Thread(target=self.p2.shoot, args=[])
            self.player2_thread.start()
        '''
        elif key==Qt.Key_8:
            self.e1_t = Thread(target=self.e1.enemy_jump, args=[])
            self.e1_t.start()
        elif key==Qt.Key_4:
            self.e1_t = Thread(target=self.e1.enemy_move_left, args=[])
            self.e1_t.start()
        elif key==Qt.Key_6:
            self.e1_t = Thread(target=self.e1.enemy_move_right, args=[])
            self.e1_t.start()
'''
        ###########pusovati ovaj kod
    def __update_enemyPosition__(self):
        while True:
            self.e1_thread = Thread(target=self.e1.pomeranje, args=[])
            self.e1_thread.start()
            self.e2_thread = Thread(target=self.e2.pomeranje, args=[])
            self.e2_thread.start()
            self.e3_thread = Thread(target=self.e3.pomeranje, args=[])
            self.e3_thread.start()
            if (self.map.enemies[0].alive == False and self.map.enemies[1].alive == False and self.map.enemies[2].alive == False):
               break
            time.sleep(2-self.brzina)


    def __pojavaSile__(self):
        time.sleep(random.randrange(3, 10))
        p = random.randrange(3)
        if (p == 0):
            c = 11
        elif (p == 1):
            c = 8
        elif (p == 2):
            c = 5
        o = random.randrange(8)
        if (o == 0):
            d = 4
        elif (o == 1):
            d = 5
        elif (o == 2):
            d = 6
        elif (o == 3):
            d = 7
        elif (o == 4):
            d = 8
        elif (o == 5):
            d = 9
        elif (o == 6):
            d = 10
        elif (o == 7):
            d = 11
        self.map.board[c][d] = 16

    def __thread_Nivo__(self):
        while True:
            if(self.map.enemies[0].alive == False and self.map.enemies[1].alive == False and self.map.enemies[2].alive == False):
                  self.map.board[self.p1.player_position[0]][self.p1.player_position[1]] = 1
                  self.map.board[self.p2.player_position[0]][self.p2.player_position[1]] = 1
                  #self.p1 = Player('zeleni', self.map, 2, 3)
                  self.p1.player_position = (14, 5)
                  #self.p2 = Player('plavi', self.map, 4, 5)
                  self.p2.player_position = (14, 14)
                  self.e1 = Enemy('benzo', self.map, 10, 11)
                  self.e1.enemy_position = (5, 5)
                  self.e2 = Enemy('boris', self.map, 10, 11)
                  self.e2.enemy_position = (5, 10)
                  self.e3 = Enemy(' bonie ', self.map, 10, 11)
                  self.e3.enemy_position = (11, 8)
                  # self.sila=Sila('sila', self.map, 16)
                  self.map.player1 = self.p1
                  self.map.player2 = self.p2
                  self.brzina = self.brzina + 0.1


                  list = []  # (self.e1,self.e2, self.e3)
                  list.append(self.e1)
                  list.append(self.e2)
                  list.append(self.e3)
                  self.map.enemies = list

                  self.map.board[5][5] = 10
                  self.map.board[5][10] = 10
                  self.map.board[11][8] = 10
                  if(self.p1.zivoti!=0):
                    self.map.board[14][5] = 2
                  if(self.p2.zivoti!=0):
                    self.map.board[14][14] = 5
                  if(self.p1.pokupioSilu==True):
                      self.p1.pokupioSilu=False
                  if (self.p2.pokupioSilu == True):
                      self.p2.pokupioSilu = False

                  self.map.update()
                  #break

        '''

              self.map.board[15][0] = 6
              self.map.board[15][1] = 6
              self.map.board[15][2] = 6

              self.map.board[15][15] = 7
              self.map.board[15][14] = 7
              self.map.board[15][13] = 7
            '''

    def closeEvent(self, event):
        self.key_notifier.die()