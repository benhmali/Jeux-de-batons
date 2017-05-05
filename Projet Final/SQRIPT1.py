from Game import *
from Player import *
import pickle

STICKS=15

Nom = input('Votre nom ? ')
player1 = HumanPlayer(Nom)
print ('Vous allez jouer en mode easy avec 15 batons')
Player2 = CPUPlayer("IA", "easy", STICKS)
whofirst = ''
while whofirst != 'oui' and whofirst != 'non' :
    whofirst = input('voulez-vous jouer en premier  oui/non  ?  ')
if (whofirst == 'non'):
        with open('data', 'rb') as inp: ns = pickle.load(inp)
        Player2.setNeuronNetwork(ns)
        Game(STICKS).start(Player2, player1, True)
else:
        with open('data', 'rb') as inp: ns = pickle.load(inp)
        Player2.setNeuronNetwork(ns)
        Game(STICKS).start(player1, Player2, True)


