from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from map import Map
from player import Player
from key_notifier import KeyNotifier
from threading import Thread
from time import sleep
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

#P1_INIT_ROW = 14
#P1_INIT_COLUMN = 1

#P2_INIT_ROW = 14
#P2_INIT_COLUMN = 14

P1_INIT_POS = (14, 5)
P2_INIT_POS = (14, 14)

class GameWindow(QMainWindow):

    win_change_signal = QtCore.pyqtSignal()

    def __init__(self, list_of_names):
        super().__init__()

        # p1 = green
        # p2 = blue

        self.map = Map()
        self.p1 = Player(list_of_names[0],self.map,2,3)
        self.p1.player_position=(14,5)
        self.p2 = Player(list_of_names[1],self.map,4,5)
        self.p2.player_position = (14,14)



        self.map.board[14][5]=2
        self.map.board[14][14]=5

        self.map.board[15][0]=6
        self.map.board[15][1]=6
        self.map.board[15][2]=6

        self.map.board[15][15]=7
        self.map.board[15][14]=7
        self.map.board[15][13]=7



        self.key_notifier = KeyNotifier()
        self.key_notifier.key_signal.connect(self.__update_position__)
        self.key_notifier.start()

        self.init_ui()







    def init_ui(self):
        self.setWindowTitle('Try to win, if u can :P')
        self.setFixedSize(SCREEN_WIDTH, SCREEN_HEIGHT)
        
        self.setCentralWidget(self.map)

    '''
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_D:
            
        
            if self.map.board[self.p1.player_position[0]][self.p1.player_position[1]+1]==0:
                    print("CAN'T MOVE, WALL")
            elif self.map.board[self.p1.player_position[0]][self.p1.player_position[1]+1]==1:
                    print("Igrac jedan->desno")
                    self.map.board[self.p1.player_position[0]][self.p1.player_position[1]]=1
                    self.map.board[self.p1.player_position[0]][self.p1.player_position[1]+1]=2
            
        elif event.key() == Qt.Key_A:
           
            if self.map.board[self.p1.player_position[0]][self.p1.player_position[1]-1]==0:
                    print("CAN'T MOVE, WALL")
            elif self.map.board[self.p1.player_position[0]][self.p1.player_position[1]-1]==1:
                    print("Igrac jedan->levo")
                    self.map.board[self.p1.player_position[0]][self.p1.player_position[1]]=1
                    self.map.board[self.p1.player_position[0]][self.p1.player_position[1]-1]=3
    '''
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
        elif key == Qt.Key_0:
            self.player2_thread = Thread(target=self.p2.shoot, args=[])
            self.player2_thread.start()
       # elif key == Qt.Key_Down:
        #    self.player2_thread = Thread(target=self.p2.moveDown, args=[])
         #   self.player2_thread.start()




        '''
        if key == Qt.Key_A:
            self.player2_thread = Thread(target=self.player2.movePlayerLeft, args=[self.player2_label, ])
            self.player2_thread.start()
        
        elif key == Qt.Key_W:
            self.player2_thread = Thread(target=self.player2.movePlayerUp, args=[self.player2_label, ])
            self.player2_thread.start()
        elif key == Qt.Key_S:
            self.player2_thread = Thread(target=self.player2.movePlayerDown, args=[self.player2_label, ])
            self.player2_thread.start()
        '''
    def closeEvent(self, event):
        self.key_notifier.die()