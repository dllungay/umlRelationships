class Room:
    def __init__(self, name):
        self.name = name

class House:
    def __init__(self):
        self.rooms = [Room("Kitchen"), Room("Bedroom")]

h = House()
print([r.name for r in h.rooms])  