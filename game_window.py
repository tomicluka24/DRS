from PyQt5.QtCore import Qt, QThread
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from map import Map
from player import Player, Enemy
from key_notifier import KeyNotifier


import time

from threading import Thread

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

# P1_INIT_ROW = 14
# P1_INIT_COLUMN = 1

# P2_INIT_ROW = 14
# P2_INIT_COLUMN = 14

P1_INIT_POS = (14, 5)
P2_INIT_POS = (14, 14)


class GameWindow(QMainWindow):
    win_change_signal = QtCore.pyqtSignal()

    def __init__(self, list_of_names):
        super().__init__()

        # p1 = green
        # p2 = blue

        self.map = Map()
        self.p1 = Player(list_of_names[0], self.map, 2, 3)
        self.p1.player_position = (14, 5)
        self.p2 = Player(list_of_names[1], self.map, 4, 5)
        self.p2.player_position = (14, 14)
        self.e1 = Enemy('benzo', self.map, 10, 11)
        self.e1.enemy_position = (5, 5)
        self.e2 = Enemy('boris', self.map, 16, 17)
        self.e2.enemy_position = (5, 10)
        self.e3 = Enemy(' bonie ', self.map, 18, 19)
        self.e3.enemy_position = (11, 8)

        self.map.board[5][5] = 10
        self.map.board[11][8] = 18
        self.map.board[14][5] = 2
        self.map.board[14][14] = 5
        self.map.board[5][10] = 16

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

        self.init_ui()

        # self.__update_enemyPosition__()

    def Protivnik(self):
        if (self.e1.enemy_position == self.p1.player_position):
            self.p1.zivoti - 1
            print("ISTI P1")
        elif self.e1.enemy_position == self.p2.player_position:
            self.p2.zivoti - 1
            # i da ga vrati na svoju poziciju nazad
            print("Isti P2")

    def init_ui(self):
        self.setWindowTitle('Try to win, if u can :P')
        self.setFixedSize(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.setCentralWidget(self.map)

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

    def __update_enemyPosition__(self):
        while (self.e1.alive == True):
            self.e1_thread = Thread(target=self.e1.pomeranje, args=[])
            self.e1_thread.start()
            self.e2_thread = Thread(target=self.e2.pomeranje, args=[])
            self.e2_thread.start()
            self.e3_thread = Thread(target=self.e3.pomeranje, args=[])
            self.e3_thread.start()
            time.sleep(2)

    def closeEvent(self, event):
        self.key_notifier.die()