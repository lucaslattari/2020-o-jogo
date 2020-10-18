from player import Player
from zone_handler import ZoneHandler
from zone import Zone

from colorama import init
init()

from colorama import Fore, Back, Style

from titleScreen import showTitleScreen

def startGame(player, global_map):
    #cria grafo do mapa inicial
    zone1 = Zone('0', "Casa")
    zone2 = Zone('1', "Quarteirão")
    zone3 = Zone('2', "Cidade")

    #atribui os nós
    global_map.addNode(zone1)
    global_map.addNode(zone2)
    global_map.addNode(zone3)

    #conecta os mapas
    global_map.addEdge(zone1, zone2)
    global_map.addEdge(zone2, zone1)
    global_map.addEdge(zone2, zone3)
    global_map.addEdge(zone3, zone2)

    #global_map.printGraph()
    #input()

    #define onde o jogador vai começar
    player.setLocation(zone1)

    print("Você acaba de acordar sem saber o que está havendo.")
    print("Ao olhar seu celular, você percebe que estamos em " + Fore.RED + "31 de dezembro de 2020." + Style.RESET_ALL)

def main():
    showTitleScreen()
    p = Player()
    global_map = ZoneHandler()

    startGame(p, global_map)

    while True:
        p.location.start()

main()
