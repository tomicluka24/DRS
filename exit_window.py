from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
SCREEN_HOR_POSITION = 350
SCREEN_VER_POSITION = 150


class ExitWindow1(QMainWindow):
	win_change_signal = QtCore.pyqtSignal()

	def __init__(self,bubnamevalue,bobnamevalue,bubpointsvalue,bobpointsvalue,oneLastedLonger):
		super().__init__()

		# Background image and pallete
		self.bImage = QImage("images/enter_names.jpg")
		self.palette = QPalette()

		# Choose name label
		#self.choose_name = QLabel('Enter names:')

		# Play button
		#self.playButton = QPushButton('Play', self)
		self.longer = QLabel(self)
		self.longer.setFixedSize(300, 60)
		if(oneLastedLonger==True):
			self.longer.setText(bubnamevalue)
			self.longer.setStyleSheet(
				"background-color: white;""font: 25pt Comic Sans MS;""color: green;""border-radius: 20px;")
		else:
			self.longer.setText(bobnamevalue)
			self.longer.setStyleSheet(
				"background-color: white;""font: 25pt Comic Sans MS;""color: blue;""border-radius: 20px;")
		# Labels for p1 and p2
		self.bub = QLabel('', self)
		self.bob = QLabel('', self)

		# Line edit fields so player can enter name
		self.bub_name = QLabel(self)
		self.bob_name = QLabel(self)

		self.bub_points = QLabel(self)
		self.bob_points = QLabel(self)

		self.bub_name.text=bubnamevalue
		self.bob_name.text=bobnamevalue
		self.bub_name.setText(bubnamevalue)
		self.bob_name.setText(bobnamevalue)
		self.bub_points.setText(str(bubpointsvalue))
		self.bob_points.setText(str(bobpointsvalue))
		# QWidget which stores buttons
		self.qWidget = QWidget()

		self.init_ui()

	def init_ui(self):
		self.setWindowTitle('Enter your names')
		self.setGeometry(SCREEN_HOR_POSITION, SCREEN_VER_POSITION, SCREEN_WIDTH, SCREEN_HEIGHT)
		self.setFixedSize(SCREEN_WIDTH, SCREEN_HEIGHT)
		self.palette.setBrush(QPalette.Window, QBrush(self.bImage))
		self.setPalette(self.palette)

		#self.playButton.setFixedSize(300, 60)
		#self.playButton.setStyleSheet("background-color: #33ffff;""font: 25pt Comic Sans MS;""color: black;""border-radius: 20px;")
		#self.playButton.clicked.connect(lambda: self.onPlayPressed())

		# Choose name style sheet
		#self.choose_name.setStyleSheet("background: transparent;""font: 25pt Comic Sans MS;""color: white;""border-radius: 20px;")
		#self.choose_name.setAlignment(Qt.AlignCenter)

		# Set icons for character's
		bub_pixmap = QPixmap('characters/bub_right.png')
		self.bub.setPixmap(bub_pixmap.scaled(60, 60, Qt.KeepAspectRatio))
		self.bub_name.setFixedSize(300, 60)
		self.bub_name.setStyleSheet(
			"background-color: white;""font: 25pt Comic Sans MS;""color: green;""border-radius: 20px;")

		self.bub_points.setFixedSize(120, 60)
		self.bub_points.setStyleSheet(
			"background-color: white;""font: 25pt Comic Sans MS;""color: green;""border-radius: 20px;")

		bob_pixmap = QPixmap('characters/bob_right.png')
		self.bob.setPixmap(bob_pixmap.scaled(60, 60, Qt.KeepAspectRatio))
		self.bob_name.setFixedSize(300, 60)
		self.bob_name.setStyleSheet(
			"background-color: white;""font: 25pt Comic Sans MS;""color: blue;""border-radius: 20px;")

		self.bob_points.setFixedSize(120, 60)
		self.bob_points.setStyleSheet(
			"background-color: white;""font: 25pt Comic Sans MS;""color: blue;""border-radius: 20px;")
		# Add horizontal layout
		p1_horizonal_layout = QHBoxLayout()
		p2_horizonal_layout = QHBoxLayout()
		p3_horizontal_layout = QHBoxLayout()
		verital_layout = QVBoxLayout()

		self.label=QLabel()
		self.label.setText("LASTED LONGER:")

		p4_horiznotal_layout =QHBoxLayout()

		self.label.setStyleSheet(
			"background-color: white;""font: 25pt Comic Sans MS;""color: black;""border-radius: 20px;")

		p4_horiznotal_layout.addStretch(1)
		p4_horiznotal_layout.addWidget(self.label)
		p4_horiznotal_layout.addWidget(self.longer)
		p4_horiznotal_layout.addStretch(1)


		p1_horizonal_layout.addStretch(1)

		p1_horizonal_layout.addWidget(self.bub)
		p1_horizonal_layout.addWidget(self.bub_name)
		p1_horizonal_layout.addWidget(self.bub_points)
		p1_horizonal_layout.addStretch(1)

		p2_horizonal_layout.addStretch(1)
		p2_horizonal_layout.addWidget(self.bob)
		p2_horizonal_layout.addWidget(self.bob_name)
		p2_horizonal_layout.addWidget(self.bob_points)
		p2_horizonal_layout.addStretch(1)

		dummy = QLabel('', self)
		dummy.setFixedSize(60, 60)
		p3_horizontal_layout.addStretch(1)
		p3_horizontal_layout.addWidget(dummy)
		#p3_horizontal_layout.addWidget(self.playButton)
		p3_horizontal_layout.addStretch(1)

		verital_layout.addStretch(1)
		#verital_layout.addWidget(self.choose_name)
		verital_layout.addLayout(p4_horiznotal_layout)
		verital_layout.addLayout(p1_horizonal_layout)
		verital_layout.addLayout(p2_horizonal_layout)
		verital_layout.addStretch(1)
		verital_layout.addLayout(p3_horizontal_layout)

		# Add layout inside widget
		self.qWidget.setLayout(verital_layout)

		# Add central widget which contains buttons
		self.setCentralWidget(self.qWidget)

	def onPlayPressed(self):
		if (self.bub_name.text().strip() == "" or self.bob_name.text().strip() == ""):
			print("Empty!")
			self.choose_name.setStyleSheet(
				"background: transparent;""font: 25pt Comic Sans MS;""color: red;""border-radius: 20px;")
			self.choose_name.setText("You must enter both names!")
		else:
			print("onPlayPressed")
			self.win_change_signal.emit()
