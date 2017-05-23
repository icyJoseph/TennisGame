"""
The class player attributes are score and name.
The class player also provides methods to:
- Increase the score
- Return the points/score of a playerA
- Return the name of a playerA
- Transform the score of a player to Tennis terms

"""

class Player:
    def __init__(self, name):
        self.score = 0
        self.name = name

    def addScore(self):
        self.score += 1
        return self.score

    def points(self):
        return self.score

    def setName(self, context):
        self.name = context
        return self.name

    def getName(self):
        return self.name

    def score2string(self):
        if self.score == 0:
            return "Love"
        elif self.score == 1:
            return "Fifteen"
        elif self.score == 2:
            return "Thirty"
        elif self.score == 3:
            return "Forty"
