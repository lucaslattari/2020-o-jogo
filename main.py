from player import Player
from zone_handler import ZoneHandler
from zone import Zone

import time, os

from colorama import init
init()

from colorama import Fore, Back, Style

def showTitleScreen():
    titleFrame1 = '''
  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$
 /$$__  $$ /$$$_  $$ /$$__  $$ /$$$_  $$
|__/  \ $$| $$$$\ $$|__/  \ $$| $$$$\ $$
  /$$$$$$/| $$ $$ $$  /$$$$$$/| $$ $$ $$
 /$$____/ | $$\ $$$$ /$$____/ | $$\ $$$$
| $$      | $$ \ $$$| $$      | $$ \ $$$
| $$$$$$$$|  $$$$$$/| $$$$$$$$|  $$$$$$/
|________/ \______/ |________/ \______/

'''
    titleFrame2 = '''
 $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\\
$$  __$$\ $$$ __$$\ $$  __$$\ $$$ __$$\\
\__/  $$ |$$$$\ $$ |\__/  $$ |$$$$\ $$ |
 $$$$$$  |$$\$$\$$ | $$$$$$  |$$\$$\$$ |
$$  ____/ $$ \$$$$ |$$  ____/ $$ \$$$$ |
$$ |      $$ |\$$$ |$$ |      $$ |\$$$ |
$$$$$$$$\ \$$$$$$  /$$$$$$$$\ \$$$$$$  /
\________| \______/ \________| \______/
'''

    titleFrame3 = '''
  ______    ______    ______    ______
 /      \  /      \  /      \  /      \\
|  $$$$$$\|  $$$$$$\|  $$$$$$\|  $$$$$$\\
 \$$__| $$| $$$\| $$ \$$__| $$| $$$\| $$
 /      $$| $$$$\ $$ /      $$| $$$$\ $$
|  $$$$$$ | $$\$$\$$|  $$$$$$ | $$\$$\$$
| $$_____ | $$_\$$$$| $$_____ | $$_\$$$$
| $$     \ \$$  \$$$| $$     \ \$$  \$$$
 \$$$$$$$$  \$$$$$$  \$$$$$$$$  \$$$$$$
'''

    titleFrame4 = '''
  ______    ______    ______    ______
 /      \  /      \  /      \  /      \\
/$$$$$$  |/$$$$$$  |/$$$$$$  |/$$$$$$  |
$$____$$ |$$$  \$$ |$$____$$ |$$$  \$$ |
 /    $$/ $$$$  $$ | /    $$/ $$$$  $$ |
/$$$$$$/  $$ $$ $$ |/$$$$$$/  $$ $$ $$ |
$$ |_____ $$ \$$$$ |$$ |_____ $$ \$$$$ |
$$       |$$   $$$/ $$       |$$   $$$/
$$$$$$$$/  $$$$$$/  $$$$$$$$/  $$$$$$/

'''
    startTime = time.time()   #Tempo de inicio
    currentTime = time.time() #Tempo atual
    counterFrame = 0
    while(currentTime < startTime + 4.0):
        if(counterFrame % 4 == 0):
            print(titleFrame1)
        elif(counterFrame % 4 == 1):
            print(titleFrame2)
        elif(counterFrame % 4 == 2):
            print(titleFrame3)
        else:
            print(titleFrame4)

        time.sleep(0.2)
        counterFrame += 1
        os.system("cls")
        currentTime = time.time()

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
    #showTitleScreen()
    p = Player()
    global_map = ZoneHandler()

    startGame(p, global_map)

    while True:
        p.location.start()

main()
