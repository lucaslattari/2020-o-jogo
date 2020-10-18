from random import randint
from colorama import Fore, Back, Style

class Zone:
    def __init__(self, key, name):
        self.key = key
        self.name = name

    def getName(self):
        return self.name

    def getKey(self):
        return self.key

    def checkAction(self, action):
        listOfActions = ['explorar', 'investigar', 'procurar']
        if action in listOfActions:
            print('Você não encontrou nada.')
        else:
            print('Ação indefinida.')

    def start(self):
        print('\nVocê está em ' + Back.WHITE + Fore.BLACK + self.name + '.' + Style.RESET_ALL)
        print("O que você deseja fazer?")
        action = input(">")
        self.checkAction(action)
