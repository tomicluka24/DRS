from PyQt5.QtWidgets import (QMainWindow, QLabel, QDesktopWidget, QFrame, QPushButton)
from PyQt5.QtGui import (QPainter, QPixmap, QIcon, QMovie, QTextDocument)
from PyQt5.QtCore import Qt, QThreadPool, pyqtSlot, QCoreApplication

P1_LIFE1_POS = (0, 15)
P1_LIFE2_POS = (1, 15)
P1_LIFE3_POS = (2, 15)

P2_LIFE1_POS = (13, 15)
P2_LIFE2_POS = (14, 15)
P2_LIFE3_POS = (15, 15)

class Map(QFrame):
    def __init__(self):
        super().__init__()
        
        # i = vertical, kolona 
        # j = horizonal, vrsta
       
        self.block_w = 75
        self.block_h = 50



        self.board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

    def paintEvent(self, event):
        #print("Event is: ", event)
        painter = QPainter(self)
        for x in range(16):
            for y in range(16):
                if self.board[x][y] == 0:
                    painter.drawPixmap(y * self.block_w, x * self.block_h, self.block_w, self.block_h, QPixmap('map/map_block.png'))
                elif self.board[x][y] == 1:
                    painter.fillRect(y * self.block_w, x * self.block_h, self.block_w, self.block_h, Qt.black)
                elif self.board[x][y] == 2:
                    painter.fillRect(y * self.block_w, x * self.block_h, self.block_w, self.block_h, Qt.black)
                    painter.drawPixmap(y * self.block_w,x * self.block_h, self.block_w, self.block_h, QPixmap('characters/bub_right.png'))
                elif self.board[x][y] == 3:
                    painter.fillRect(y * self.block_w, x * self.block_h, self.block_w, self.block_h, Qt.black)
                    painter.drawPixmap(y * self.block_w, x * self.block_h, self.block_w, self.block_h, QPixmap('characters/bub_left.png'))
                elif self.board[x][y] == 4:
                    painter.fillRect(y * self.block_w, x * self.block_h, self.block_w, self.block_h, Qt.black)
                    painter.drawPixmap(y * self.block_w, x * self.block_h, self.block_w, self.block_h, QPixmap('characters/bob_right.png'))
                elif self.board[x][y] == 5:
                    painter.fillRect(y * self.block_w, x * self.block_h, self.block_w, self.block_h, Qt.black)
                    painter.drawPixmap(y * self.block_w, x * self.block_h, self.block_w, self.block_h, QPixmap('characters/bob_left.png'))
                elif self.board[x][y] == 6:
                    painter.drawPixmap(y * self.block_w, x * self.block_h, self.block_w, self.block_h, QPixmap('map/map_block.png'))
                    painter.drawPixmap(y * self.block_w, x * self.block_h, self.block_w, self.block_h, QPixmap('characters/bub_right.png'))
                elif self.board[x][y] == 7:
                    painter.drawPixmap(y * self.block_w, x * self.block_h, self.block_w, self.block_h, QPixmap('map/map_block.png'))
                    painter.drawPixmap(y * self.block_w, x * self.block_h, self.block_w, self.block_h, QPixmap('characters/bob_left.png'))
                elif self.board[x][y] == 8:
                    painter.fillRect(y * self.block_w, x * self.block_h, self.block_w, self.block_h, Qt.black)
                    painter.drawPixmap(y * self.block_w, x * self.block_h, self.block_w, self.block_h, QPixmap('images/green_bubble1.png'))
                elif self.board[x][y] == 9:
                    painter.fillRect(y * self.block_w, x * self.block_h, self.block_w, self.block_h, Qt.black)
                    painter.drawPixmap(y * self.block_w, x * self.block_h, self.block_w, self.block_h, QPixmap('images/blue_bubble.png'))

        self.update()