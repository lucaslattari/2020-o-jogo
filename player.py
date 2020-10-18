class Player:
    def __init__(self):
        self.name = input("Informe o nome do jogador(a): ")
        self.level = 1
        self.hp = 100
        self.mp = 0
        self.inventory = {}

    def setLocation(self, zone):
        self.location = zone

    def getLocation(self):
        return self.location

    def levelUp(self):
        self.level += 1

    def damage(self):
        self.hp -= 10
        if (self.hp < 0):
            self.die()

    def die(self):
        self.hp = 0
        print("WASTED")

    # def pickUpItem(self, item):

    # def showItems(self):

    # def dropItem(self, item):
