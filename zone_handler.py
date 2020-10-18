from random import randint
from zone import Zone

class ZoneHandler:
    def __init__(self):
        self.zones = []
        self.ways = {}

    def add(self, zone):
        self.zones.append(zone)

    def addListOf(self, zones):
        for zone in zones:
            self.add(zone)

    def connectUnidirectionally(self, zone1, zone2):
        if zone1.key not in self.ways:
            self.ways[zone1.key] = [zone2]
        else:
            self.ways[zone1.key].append(zone2)

    def connect(self, zone1, zone2):
        self.connectUnidirectionally(zone1, zone2)
        self.connectUnidirectionally(zone2, zone1)

    def getZone(self, key):
        return self.zones[key]

    def printGraph(self):
        for key, list_values in self.ways.items():
            for value in list_values:
                print(key, value.key)
