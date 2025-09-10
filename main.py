from objects.graph import Graph
from system.loadFile import *

from chars.minotaur import *
from chars.labyrinthGuy import *
# g = Graph(1, 4, 3, 5)
# for node in g.vertices:
#     print(node.nodeID, node.adjascentVertices)

# g.setNodeInfo({1: {2:4, 3:2, 0:2, 4:3}, 0: {2:3, 4:3}})
# for node in g.vertices:
#     print(node.nodeID, node.adjascentVertices)

class Main:
    def __init__(self, fileLocation: str = "graph.json"):
        loadSys = LoadFileSystem(fileLocation)

        self.minotaur = Minotaur(loadSys.content["minotaurInitialPos"], loadSys.content["minotaurDetectionDistance"])
        self.labyrinthGuy = LabyrinthGuy(loadSys.content["enterVertex"])

        self.graph: Graph = Graph(loadSys.content["enterVertex"], loadSys.content["exitVertex"], loadSys.content["numVertices"])
        self.graph.setNodeInfo(loadSys.content["edgeList"])

        self.iterationCounter: int = 0
        self.runIteration(self.iterationCounter)

    def runIteration(self, counter: int) -> None:
        """
        1 - mover entrante\n
        2 - mover minotauro\n
        3 - checar saída no entrante\n
        4 - checar detecção no minotauro\n
        5 - checar se ambos estão no mesmo lugar\n
        6 - processar batalha\n
        7 - diminuir suprimentos\n
        """
        pass

Main()