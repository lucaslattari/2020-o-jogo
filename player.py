class Player:
    def __init__(self):
        self.name = input("Informe o nome do jogador ou jogadora: ")
        self.level = 1
        self.hp = 100
        self.mp = 0
        self.inventory = {}

    def setLocation(self, zone):
        self.location = zone

    def getLocation(self):
        return self.location
