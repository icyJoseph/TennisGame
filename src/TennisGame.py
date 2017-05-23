from Player import Player
from Set import Set

"""
The TennisGame class is instantiated by inputing the name of the players.

The TennisGame class instantiates the Set class with two player objects

The TennisGame class implements the following methods:
- getName methods to either get both player names or a player name at a time
- setNames method to "set" the name of the players
    * If the names are the same or equal to "", the method takes default names
- score, method that returns the current score of the game
- addScore, method used to increment the score/points of a player
- isSetOver, method to indicate that the set is over
"""

class TennisGame:
    def __init__(self):
        self.playerA = Player("playerA")
        self.playerB = Player("playerB")
        self.set = Set(self.playerA, self.playerB)

    def getNames(self):
        return self.getNamePlayerA() + " vs " + self.getNamePlayerB()

    def getNamePlayerA(self):
        return self.playerA.getName()

    def getNamePlayerB(self):
        return self.playerB.getName()

    def setNames(self):
        nameA = input("First player name? ")
        if nameA == "":
            nameA = "playerA"
        print(nameA)
        nameB = input("Second player name? ")
        if nameB == "":
            nameB = "playerB"
        print(nameB)
        if nameA == nameB:
            print("The names were the same, using default names")
        elif nameA != nameB:
            self.playerA.setName(nameA)
            self.playerB.setName(nameB)

        print(self.getNames())

    def score(self):
        print (self.set.result())

    def addScore(self, scorer):
        if scorer == self.playerA.name:
            return self.playerA.addScore()
        elif scorer == self.playerB.name:
            return self.playerB.addScore()

    def isSetOver(self):
        return self.set.isSetOver()
