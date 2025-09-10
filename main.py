from objects.graph import Graph
from system.loadFile import *

# g = Graph(1, 4, 3, 5)
# for node in g.vertices:
#     print(node.nodeID, node.adjascentVertices)

# g.setNodeInfo({1: {2:4, 3:2, 0:2, 4:3}, 0: {2:3, 4:3}})
# for node in g.vertices:
#     print(node.nodeID, node.adjascentVertices)

class Main:
    def __init__(self, fileLocation: str = "graph.json"):
        loadSys = LoadFileSystem(fileLocation)
        graph: Graph = Graph(loadSys.content["enterVertex"], loadSys.content["exitVertex"], loadSys.content["minotaurInitialPos"], loadSys.content["numVertices"])
        graph.setNodeInfo(loadSys.content["edgeList"])

        self.iterationCounter: int = 0
        self.runIteration(self.iterationCounter)
        for i in range(len(graph.vertices)):
            print(graph.vertices[i])

    def runIteration(self, counter: int) -> None:
        pass

Main()