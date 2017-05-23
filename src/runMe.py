from TennisGame import TennisGame
"""
use:
python -B runme.py

*this code is writen for python 3+

"""
W = TennisGame()
W.setNames()
print("Type in the name of whoever scores.")
while W.isSetOver() is False:
    scorer = input("Who scored? ")
    if scorer == W.getNamePlayerA() or scorer == W.getNamePlayerB():
        W.addScore(scorer)
        W.score()
    else:
        print (scorer+" is an incorrect name")
