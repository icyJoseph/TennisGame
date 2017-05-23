"""
The Set class brings together two player objects. Composition.

A Tennis game may have many sets. That is part of a future implementation.

The Set class has many private methods:
- __deuceFlag, private method to indicate that the score may be Deuce if the
    players have the same score

- __advFlag, private method to indicate that either player may have advantage
    over the other

- __diff, private method that returns the absolute difference between scores

- __greater, private method that returns a flag indicating that player A has a
    higher score than player B

Finally, the Set class has two methods to reflect the status of the Set:
- result, method that returns the score of the set in tennis terms
- isSetOver, method returns a flag indicating whether or not the game is over,
  according to tennis rules.
"""

class Set:
    def __init__(self, playerA, playerB):
        self.playerA = playerA
        self.playerB = playerB
        self.setOver = False

    def __deuceFlag(self):
        return max(self.playerA.points(), self.playerB.points()) >= 3

    def __advFlag(self):
        return max(self.playerA.points(), self.playerB.points()) > 3

    def __diff(self):
        return abs(self.playerA.points() - self.playerB.points())

    def __greater(self):
        return self.playerA.points() > self.playerB.points()

    def result(self):
        if self.__deuceFlag():
            if self.__diff() == 0:
                return "DEUCE"
        if self.__advFlag():
            if self.__diff() == 1:
                if self.__greater():
                    return self.playerA.name + " ADV"
                else:
                    return self.playerB.name + " ADV"
            elif self.__diff() > 1:
                self.setOver = True
                if self.__greater():
                    return self.playerA.name + " WINS"
                else:
                    return self.playerB.name + " WINS"

        else:
            return (self.playerA.name + ": " + self.playerA.score2string() + " - "
                + self.playerB.name+ ": " + self.playerB.score2string())

    def isSetOver(self):
        return self.setOver
