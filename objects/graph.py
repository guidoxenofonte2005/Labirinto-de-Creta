import heapq
from functools import singledispatchmethod

from objects.node import Node

class Graph():
    def __init__(self, labyrinthStart: int, labyrinthEnd: int, graphSize: int):
        self.vertices: list[Node] = [Node(i, {}) for i in range(graphSize)]
        self.start = labyrinthStart
        self.end = labyrinthEnd
        # print(self.vertices)
    

    # @setNodeInfo.register
    def setNodeInfo(self, nodeInfo: dict) -> None:
        for node, info in nodeInfo.items():
            newAdjascencies = {}
            for vertex, weight in info.items():
                newAdjascencies[vertex] = weight
            self.vertices[int(node)].setAdjascencies(newAdjascencies)
        
        for node in self.vertices:
            for object, adjacencies in node.adjascentVertices.items():
                if node.nodeID not in self.vertices[int(object)].adjascentVertices.keys():
                    self.vertices[int(object)].adjascentVertices[node.nodeID] = adjacencies

    # algoritmo de dijkstra
    def findNode(self, startNode: Node, searchedNode: Node) -> int:
        distance: list[int] = [1e7] * len(self.vertices)
        # print(type(startNode), type(searchedNode))
        distance[startNode.nodeID] = 0
        
        heap = [(0, startNode.nodeID)]

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
                    # print(f"Índice {e} não encontrado")
                    pass

        try:
            return distance[int(searchedNode.nodeID)]
        except IndexError as e:
            pass

    def findPath(self, startNode: Node, searchedNode: Node) -> list[Node]:
        distance: list[int] = [1e7] * len(self.vertices)
        distance[startNode.nodeID] = 0

        fatherNode = {startNode.nodeID: None}
        
        heap = [(0, startNode.nodeID)]

        while heap:
            currentCost, currentVertex = heapq.heappop(heap)

            if currentVertex == searchedNode:
                break
            
            if currentCost > distance[currentVertex]:
                continue

            for item in self.vertices:
                try:
                    if distance[currentVertex] + item.adjascentVertices[currentVertex] < distance[item.nodeID]:
                        distance[item.nodeID] = distance[currentVertex] + item.adjascentVertices[currentVertex]
                        fatherNode[item.nodeID] = currentVertex
                        heapq.heappush(heap, (distance[item.nodeID], item.nodeID))
                except KeyError as e:
                    # print(f"Índice {e} não encontrado")
                    pass

        if distance[searchedNode.nodeID] >= 1e7: return None

        path: list[Node] = []
        currentVertex = searchedNode.nodeID
        while currentVertex is not None:
            path.append(self.vertices[currentVertex])
            currentVertex = fatherNode[currentVertex]
        path.reverse()
        
        return path