import heapq
from functools import singledispatchmethod

from chars.minotaur import *
from objects.node import *

class Graph():
    def __init__(self, labyrinthStart: int, labyrinthEnd: int, startMinotaurPos: int, graphSize: int):
        self.vertices: list[Node] = [Node(_, {}) for _ in range(graphSize)]
        self.minotaur: Minotaur = Minotaur(startMinotaurPos, 10)
        self.start = labyrinthStart
        self.end = labyrinthEnd
    
    # @singledispatchmethod
    # def setNodeInfo(self, nodeInfo) -> None:
    #     raise TypeError(f"Unsupported type: {type(nodeInfo)}")
    
    # @setNodeInfo.register
    # def setNodeInfo(self, node: int, nodeInfo: tuple[int, int]) -> float:
    #     """
    #     """

    # @setNodeInfo.register
    def setNodeInfo(self, nodeInfo: dict) -> None:
        """
        Passes the node info down to every single node in graph
        @param nodeInfo: Information about the nodes, using the following json structure:\n
        nodeID: {\n
            vertex: weight\n
        }
        """
        for node, info in nodeInfo.items():
            newAdjascencies = {}
            for vertex, weight in info.items():
                newAdjascencies[vertex] = weight
            self.vertices[node].setAdjascencies(newAdjascencies)
        
        for node in self.vertices:
            for i in range(len(self.vertices)):
                if i == node.nodeID: continue

                next = self.vertices[i % len(self.vertices)]
                if node.nodeID in next.adjascentVertices and next.nodeID not in node.adjascentVertices:
                    node.adjascentVertices[next.nodeID] = next.adjascentVertices[node.nodeID]

    # fazer dentro de outra classe
    def runIteration(self) -> None:
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

    # algoritmo de dijkstra
    def findNode(self, startNode: int, searchedNode: int) -> int:
        """
        Uses Dijkstra's algorithm to calculate said distance\n
        Returns the distance between two known nodes as an integer\n
        @param startNode: (int) Index of starting node
        @param searchedNode: (int) Index of the node who's being searched
        """
        distance: list[int] = [1e7] * len(self.vertices)
        distance[startNode] = 0
        
        heap = [(0, startNode)]

        while heap:
            currentCost, w = heapq.heappop(heap)

            if currentCost > distance[w]:
                continue

            for item in self.vertices:
                try:
                    if distance[w] + item.adjascentVertices[w] < distance[item.nodeID]:
                        distance[item.nodeID] = distance[w] + item.adjascentVertices[w]
                        heapq.heappush(heap, (distance[item.nodeID], item.nodeID))
                except KeyError as e:
                    print(f"Índice {e} não encontrado")

        return distance[searchedNode]