from chars.baseChar import *
from objects.node import Node
from objects.graph import Graph

from random import randint

class Minotaur(BaseChar):
    def __init__(self, initialPos: Node, detectionDistance: int):
        super().__init__(initialPos)
        self.detectionDistante = detectionDistance
        self.DETECTED_PLAYER = False
        self.pursuitOrderArray: list[Node] = []

    def characterCheck(self, minDistanceToPlayer: int):
        self.DETECTED_PLAYER = minDistanceToPlayer <= self.detectionDistante

    def combat(self) -> bool:
        return randint(1, 100) == 1
    
    def move(self, currentNode: Node, graph: Graph, chaseNode: Node = None):
        if not self.DETECTED_PLAYER:
            return super().move(currentNode)
        
        path = graph.findPath(currentNode, chaseNode)
        if path == None:
            return super().move(currentNode)

        self.pursuitOrderArray.append(path[:2] if len(path) > 2 else path)
        self.position = self.pursuitOrderArray[-1]