class Player:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self, players):
        self.players = players

p1, p2 = Player("Ann"), Player("Ben")
team = Team([p1, p2])
del team
print(p1.name) 