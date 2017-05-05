import random

BASE_WEIGHT = 10
RECOMPENSE = 8

class NeuronNetwork:
    def __init__(self,maxDist,nbSticks):
        self.neurons = []
        for i in range(1,nbSticks+1):
            self.neurons.append(Neuron(self,i))
        for neuron in self.neurons:
            neuron.makeConnections(maxDist,nbSticks,BASE_WEIGHT)
        self.initPath()
    def initPath(self):
        self.path = {}
    def getNeuron(self,index):
        if index-1>=0 and index<=len(self.neurons): return self.neurons[index-1]
        else: return None
    def activateNeuronPath(self,neuron1,neuron2):
        self.path[neuron1]=neuron2
    def recompenseConnections(self):
        for neuron1,neuron2 in self.path.items():
            neuron1.recompenseConnection(neuron2)
        self.initPath()
    def printAllConnections(self):
        for neuron in self.neurons: neuron.printConnections()
    def printScores(self):
        scores = {}
        for neuron in self.neurons:
            for n,s in neuron.connections.items():
                if n not in scores: scores[n]=s
                else: scores[n] = scores[n] + s
        for neuron,score in scores.items():
            print(neuron.asString(),score)

class Neuron:
    def __init__(self,network,index):
        self.network = network
        self.index = index
        self.connections = {}
    def makeConnections(self,maxDist,nbSticks,baseWeight):
        if self.index!=nbSticks: nb=maxDist*2 +1
        else: nb=maxDist +1
        for i in range(1,nb):
            neuron = self.network.getNeuron(self.index-i)
            if neuron!=None: self.connections[neuron]=baseWeight
    # TODO méthode qui retourne un neurone connecté au neurone actuel en fonction du 'shift' (cf. CPUPlayer).
    # On devra utiliser la méthode self.weighted_choice pour choisir au hasard dans une liste de connexions disponibles en fonction de leurs poids
    def chooseConnectedNeuron(self,shift):
        connections = self.connections.copy()
        neuron = self.weighted_choice(connections)
        while not neuron == None and not neuron.testNeuron(self.index - shift):
            connections.pop(neuron)
            neuron = self.weighted_choice(connections)
        return neuron
		# TODO renvoie un booléen : True si la différence entre la 'inValue' et la valeur du neurone actuel est comprise entre 1 et 3 inclus
	def testNeuron(self,inValue):
                        return (inValue - self.index) in range(1, 4)
#cette methode permet d'ajouter du poids à une connection s'il permet la victoire.
    def recompenseConnection(self,neuron):
        self.connections[neuron] = self.connections[neuron] + RECOMPENSE
#cette methode permet d'afficher les connections entre les neuronnes.
    def printConnections(self):
        print("Connections of",self.asString()+":")
        for neuron in self.connections:
            print(neuron.asString(),self.connections[neuron])
    def asString(self):
        return "N"+str(self.index)
# cette méthode permet de faire des choix en fonctions des forts poids 
    def weighted_choice(self,connections):
       total = sum(w for c, w in connections.items())
       r = random.uniform(0, total)
       upto = 0
       for c, w in connections.items():
          if upto + w >= r: return c
          upto += w
        


        


