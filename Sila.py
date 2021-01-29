from PyQt5.QtWidgets import QLabel, QWidget
from time import sleep

class Sila(QLabel):
    def __init__(self, name, mapa, a):
        super().__init__()
        self.player_name = name
        self.player_position = ()
        self.mapa = mapa
        self.a = a




