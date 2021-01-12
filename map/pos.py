class Position():
    def __init__(self):
        self.row = -1
        self.column = -1
        self.available = False
        self.player = False
        self.enemy = False

    def setPosition(self, position, available, player, enemy):
        self.row = position[0]
        self.column = position[1]

    def print(self):
        print(self.row, self.column, self.available, self.player, self.enemy)