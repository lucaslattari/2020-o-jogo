from random import randint
from zone import Zone

class ZoneHandler:
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def addNode(self, zone):
        self.nodes.append(zone)

    def addEdge(self, zone1, zone2):
        if zone1.key not in self.edges:
            self.edges[zone1.key] = [zone2]
        else:
            self.edges[zone1.key].append(zone2)

    def getZone(self, key):
        return self.nodes[key]

    def printGraph(self):
        for key, list_values in self.edges.items():
            for value in list_values:
                print(key, value.key)
