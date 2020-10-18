from player import Player
from zone_handler import ZoneHandler

from colorama import init
init()

from titleScreen import showTitleScreen
from startGame import startGame

def main():
    showTitleScreen()
    p = Player()
    global_map = ZoneHandler()

    startGame(p, global_map)

    while True:
        p.location.start()

main()
