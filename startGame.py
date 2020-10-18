from zone import Zone
from colorama import Fore, Back, Style

def startGame(player, global_map):
    #cria grafo do mapa inicial
    zones = []
    zones.append(Zone('0', "Casa"))
    zones.append(Zone('1', "Quarteirão"))
    zones.append(Zone('2', "Cidade"))

    #adiciona as zonas ao mapa
    global_map.addListOf(zones)

    #conecta as zonas
    global_map.connect(zones[0], zones[1])
    global_map.connect(zones[1], zones[2])

    #global_map.printGraph()
    #input()

    #define onde o jogador vai começar
    player.setLocation(zones[1])

    print("Você acaba de acordar sem saber o que está havendo.")
    print("Ao olhar seu celular, você percebe que estamos em " + Fore.RED + "31 de dezembro de 2020." + Style.RESET_ALL)
