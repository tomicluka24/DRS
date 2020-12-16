from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap, QPainter


class Map(QWidget):
    def __init__(self):
        super().__init__()
        self.image = QPixmap('800x600-black-solid-color-background.png')
        self.setFixedSize(self.image.size())

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)
        painter.drawPixmap(0, -2, 30, 601, QPixmap('../DRSPreplanuliTraktoristi/images/picture1.png'))
        painter.drawPixmap(30, -2, 740, 30, QPixmap('../DRSPreplanuliTraktoristi/images/picture2.png'))
        painter.drawPixmap(770, -2, 30, 601, QPixmap('../DRSPreplanuliTraktoristi/images/picture3.png'))
        painter.drawPixmap(30, 569, 740, 30, QPixmap('../DRSPreplanuliTraktoristi/images/picture4.png'))
        painter.drawPixmap(150, 150, 500, 30, QPixmap('../DRSPreplanuliTraktoristi/images/picture5.png'))
        painter.drawPixmap(150, 300, 500, 30, QPixmap('../DRSPreplanuliTraktoristi/images/picture6.png'))
        painter.drawPixmap(150, 450, 500, 30, QPixmap('../DRSPreplanuliTraktoristi/images/picture7.png'))
        painter.drawPixmap(30, 150, 30, 30, QPixmap('../DRSPreplanuliTraktoristi/images/picture8.png'))
        painter.drawPixmap(30, 300, 30, 30, QPixmap('../DRSPreplanuliTraktoristi/images/picture9.png'))
        painter.drawPixmap(30, 450, 30, 30, QPixmap('../DRSPreplanuliTraktoristi/images/picture10.png'))
        painter.drawPixmap(740, 150, 30, 30, QPixmap('../DRSPreplanuliTraktoristi/images/picture11.png'))
        painter.drawPixmap(740, 300, 30, 30, QPixmap('../DRSPreplanuliTraktoristi/images/picture12.png'))
        painter.drawPixmap(740, 450, 30, 30, QPixmap('../DRSPreplanuliTraktoristi/images/picture13.png'))