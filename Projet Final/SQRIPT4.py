from Game import *
from Player import *
import pickle

STICKS=15

Nom = input('Votre nom ? ')
player1 = HumanPlayer(Nom)
mode = ''
while mode != 'easy' and mode != 'medium' and mode != 'hard' :
    mode = input('Choisir un mode de jeu parmi ces modes {easy, medium, hard}  : ')
if(mode == "easy"):
        print (' \nVous avez choisi le mode easy')
        Player2 = CPUPlayer("IA", mode, STICKS)
if(mode == "medium"):
        print (' \nVous avez choisi le medium')
        Player2 = CPUPlayer("IA", mode, STICKS)
if(mode == "hard"):
        print (' \nVous avez choisi le mode hard')
        Player2 = CPUPlayer("IA", mode, STICKS)
whofirst = ''
while whofirst != 'oui' and whofirst != 'non' :
    whofirst = input('voulez-vous jouer en premier  oui/non  ? ')
if (whofirst == 'non'):
        with open('data', 'rb') as inp: ns = pickle.load(inp)
        Player2.setNeuronNetwork(ns)
        Game(STICKS).start(Player2, player1, True)
else:
        with open('data', 'rb') as inp: ns = pickle.load(inp)
        Player2.setNeuronNetwork(ns)
        Game(STICKS).start(player1, Player2, True)


