from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import exit_window
import main_menu
import enter_names_menu
import game_window
import sys


class WindowController:

    def __init__(self):
        self.main_menu = main_menu.MainWindow()
        self.enter_names_menu = enter_names_menu.EnterNamesWindow()

    def show_main_menu(self):
        #If play is pressed we need to show play_menu
        self.main_menu.win_change_signal.connect(self.show_enter_names_menu)
        self.main_menu.show()

    def show_enter_names_menu(self):
        # When play is pressed we need to start game
        self.enter_names_menu.win_change_signal.connect(self.show_game)
        # Close main menu
        self.main_menu.close()
        self.enter_names_menu.show()

    def show_game(self):
        # Close enter names window
        self.enter_names_menu.close()
        p1_name = self.enter_names_menu.bub_name.text().strip()
        p2_name = self.enter_names_menu.bob_name.text().strip()
        self.game_window = game_window.GameWindow([p1_name, p2_name])
        self.game_window.win_change_signal.connect(self.show_end_screen)
        self.game_window.show()

    def show_end_screen(self):

        print("Showing end screen")
        bubovo_ime = self.game_window.p1.player_name
        bobovo_ime = self.game_window.p2.player_name
        print("AAA")
        bubovi_poeni = self.game_window.p1.points

        print("AAA1")
        bobovi_poeni = self.game_window.p2.points


        longer=self.game_window.player1LastedLonger
        print("AAA2")
        self.game_window.close()
        print("AAA3")


        self.endscreen=exit_window.ExitWindow1(bubovo_ime,bobovo_ime,bubovi_poeni,bobovi_poeni,longer)


        print("BBB")
        #self.endscren.bub_name.text=bubovo_ime
        print("AAA")
        self.endscreen.show()

        print("Prikaz end skrina")

if __name__ == '__main__':

    App = QApplication(sys.argv)

    windowController = WindowController()
    
    windowController.show_main_menu()
    
    #start
    sys.exit(App.exec())