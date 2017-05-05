from Game import Game
from Player import CPUPlayer
from Player import HumanPlayer
import pickle
STICKS_NB = 15

player1 = CPUPlayer("CPU1_hard", "hard", STICKS_NB)
player2 = CPUPlayer("CPU2_hard", "hard", STICKS_NB)

game = Game(STICKS_NB)

print ('script pour jouer 800 partie CPU contre lui meme dans le mode hard ')

with open('data', 'rb') as inp: ns = pickle.load(inp)
player2.setNeuronNetwork(ns)
player2.nbWin=0
for i in range(0, 800):

                game.start(player2, player1, False)
print(player1.name, '  :' ,player1.nbWin, "-", player2.nbWin, ' :' ,player2.name)

