from enum import Enum

class EDGE_INFO(Enum):
    NEXT = 0
    WEIGHT = 1

class Node():
    def __init__(self, newID: int, adjascencies: dict):
        self.nodeID: int = newID
        self.adjascentVertices: dict = adjascencies # next vertex / weight
    
    def setAdjascencies(self, newAdjascencies: dict):
        self.adjascentVertices = newAdjascencies