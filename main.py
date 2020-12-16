from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QStackedWidget, QPushButton, QDesktopWidget
from PyQt5.QtGui import QIcon
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralWidget = QStackedWidget()
        self.setCentralWidget(self.centralWidget)
        self.mainMenuWidget = MainMenu()

        self.menu()

        self.setWindowTitle('Bubble Bobble')
        self.setWindowIcon(QIcon('icon.png'))

        self.show()

    def center1(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2), int((screen.height() - size.height()) / 2))

    def menu(self):
        self.mainMenuWidget.quitGameSignal.connect(self.quit)

        self.centralWidget.addWidget(self.mainMenuWidget)
        self.centralWidget.setCurrentWidget(self.mainMenuWidget)

        self.resize(340, 280)
        self.center1()

    @staticmethod
    def quit():
        sys.exit()


class MainMenu(QWidget):

    quitGameSignal = pyqtSignal()

    def __init__(self):
        super(MainMenu, self).__init__()

        button_width = 190
        button_height = 50
        button_left = 80
        button_top = 70

        self.play_button = QPushButton('Play', self)
        self.play_button.setFixedWidth(button_width)
        self.play_button.setFixedHeight(button_height)
        self.play_button.move(button_left, button_top)

        quit_button = QPushButton('Quit', self)
        quit_button.setFixedWidth(button_width)
        quit_button.setFixedHeight(button_height)
        quit_button.move(button_left, button_top * 2)
        quit_button.clicked.connect(self.quit)

        self.show()

    def quit(self):
        self.quitGameSignal.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
