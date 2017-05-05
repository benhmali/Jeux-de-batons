from Game import Game
from Player import CPUPlayer
from Player import HumanPlayer
import pickle
STICKS_NB = 15

player1 = CPUPlayer("CPU1_hard", "hard", STICKS_NB)
player2 = CPUPlayer("CPU2_hard", "hard", STICKS_NB)
player3 = CPUPlayer("CPU3_medium", "medium", STICKS_NB)
player4 = CPUPlayer("CPU4_medium", "medium", STICKS_NB)
player5 = CPUPlayer("CPU5_easy", "easy", STICKS_NB)
player6 = CPUPlayer("CPU6_easy", "easy", STICKS_NB)

game = Game(STICKS_NB)

print ('script pour jouer 800 partie CPU contre lui meme dans les deffirent modes ')


for i in range(0, 800):

                game.start(player5, player6, False)
print(player5.name, '  :' ,player5.nbWin, "-", player6.nbWin, ' :' ,player6.name)
player5.nbWin=0
for i in range(0, 800):

                game.start(player5, player4, False)
print(player5.name, '  :' ,player5.nbWin, "-", player4.nbWin, ' :' ,player4.name)

with open('data', 'rb') as inp: ns = pickle.load(inp)
player2.setNeuronNetwork(ns)
player5.nbWin=0
for i in range(0, 800):

                game.start(player2, player5, False)
print(player5.name, '  :' ,player5.nbWin, "-", player2.nbWin, ' :' ,player2.name)
player5.nbWin=0
player2.nbWin=0
player3.nbWin=0
player4.nbWin=0
for i in range(0, 800):

                game.start(player3, player4, False)
print(player3.name, ':' ,player3.nbWin, "-", player4.nbWin, ' :' ,player4.name)

with open('data', 'rb') as inp: ns = pickle.load(inp)
player2.setNeuronNetwork(ns)
player3.nbWin=0
player4.nbWin=0
for i in range(0, 800):

                game.start(player2, player3, False)
print(player3.name, ':' ,player3.nbWin, "-", player2.nbWin, ' :' ,player2.name)

with open('data', 'rb') as inp: ns = pickle.load(inp)
player2.setNeuronNetwork(ns)
player2.nbWin=0
for i in range(0, 800):

                game.start(player2, player1, False)
print(player1.name, '  :' ,player1.nbWin, "-", player2.nbWin, ' :' ,player2.name)

