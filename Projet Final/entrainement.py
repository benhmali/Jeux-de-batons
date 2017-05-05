from Game import Game
from Player import CPUPlayer
from Player import HumanPlayer
import pickle

STICKS_NB = 15

player1 = CPUPlayer("CPU1", "hard", STICKS_NB)
player2 = CPUPlayer("CPU2", "hard", STICKS_NB)

game = Game(STICKS_NB)

for i in range(1, 1000000):
    game.start(player1, player2, False)
    print (i)
print(player1.name, ':' ,player1.nbWin, "-", player2.name, ':' ,player2.nbWin)
#save the data
with open("data",'wb') as output: pickle.dump(player1.getNeuronNetwork(), output, pickle.HIGHEST_PROTOCOL)

