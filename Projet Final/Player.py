import random
from Neuron import *


# classe mère permet de définir un player humain ou IA( CPU ) 
class Player:
    def __init__(self,name):
        self.name = name
        self.nbWin = 0
    def getName(self):
        return self.name
    def getNbWin(self):
        return self.nbWin
    def addWin(self):
        self.nbWin+=1
    def addLoss(self):
        pass
# classe  permet de définir un player humain
class HumanPlayer(Player):
    # La méthode play permet de récupérer l'entrée utilisateur et jouer le nb choisi avec un controle de saisee 
    def play(self,sticks):
        if sticks==1: return 1
        else:
            correct = False
            while not correct:
                nb = input('Sticks?\n')
                try:
                    nb=int(nb)
                    if nb>=1 and nb<=3 and sticks-nb>=0:
                        correct=True
                except: pass
            return nb
# classe  permet de définir un player IA
class CPUPlayer(Player):
    def __init__(self,name,mode,nbSticks):
        super().__init__(name)
        self.mode = mode
        self.netw = NeuronNetwork(3,nbSticks)
        self.previousNeuron = None
# selon le mode cette methode return la methode qui va choisir le nb a jouer
    def play(self,sticks):
        if self.mode=='easy': return self.playEasy(sticks)
        elif self.mode=='hard': return self.playHard(sticks)
        else: return self.playMedium(sticks)
# mode Medium avec 2 condition pour ne pas faire des gros erreur dans les deriere tours 
    def playMedium(self,sticks):
        if sticks==3: move=2
        elif sticks==4: move=3
        elif sticks==2: move=1
        else:   move=random.randint(1,3)
        return move
# mode easy qui return la methode qui jeu aléatoirement  
    def playEasy(self,sticks):
        return self.playRandom(sticks)
# qui return un nb aléatoirement mais valide ( entre 1 et 3 et entre 1 et le nb de sticks si se dernier <  4 )
    def playRandom(self,sticks):
        if sticks<4:    return random.randint(1,sticks)
        else:   return random.randint(1,3)
# TODO utiliser le réseau neuronal pour choisir le nombre de bâtons à jouer
        # utiliser l'attribut self.previousNeuron pour avoir le neuron précédemment sollicité dans la partie
        # calculer un 'shift' qui correspond à la différence entre la valeur du précédent neurone et le nombre de bâtons encore en jeu
        # utiliser la méthode 'chooseConnectedNeuron' du self.previousNeuron puis retourner le nombre de bâtons à jouer
        # bien activer le réseau de neurones avec la méthode 'activateNeuronPath' après avoir choisi un neurone cible
        # attention à gérer les cas particuliers (premier tour ou sticks==1) 
   
   def playHard(self,sticks):
        nb = 0
        if self.previousNeuron == None:
            currentNeuron = self.netw.getNeuron(sticks)
            neuron = currentNeuron.chooseConnectedNeuron(0)
            nb = sticks - neuron.index
            self.netw.activateNeuronPath(currentNeuron, neuron)
            self.previousNeuron = neuron
        else:
            shift = self.previousNeuron.index - sticks
            neuron = self.previousNeuron.chooseConnectedNeuron(shift)
            if not neuron == None:
                nb = sticks - neuron.index
                self.netw.activateNeuronPath(self.previousNeuron, neuron)
                self.previousNeuron = neuron
            else:
                nb = 1
        return nb
    def getNeuronNetwork(self): return self.netw
    def setNeuronNetwork(self,ns): self.netw = ns
# La méthode addWin permet d'incrémenter le nombre de victoire d'un joueur.
    def addWin(self):
        super().addWin()
        self.netw.recompenseConnections()
        self.previousNeuron=None
# La méthode addLoss permet de décrementer le nombre de victoire d'un joueur.
    def addLoss(self):
        super().addLoss()
        self.previousNeuron=None




        


