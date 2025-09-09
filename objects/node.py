from enum import Enum

class EDGE_INFO(Enum):
    NEXT = 0
    WEIGHT = 1

class Node():
    def __init__(self, newID: int, adjascencies: list[dict[int:int]]):
        self.nodeID: int = newID
        self.adjascentVertices: list[dict[int:int]] = adjascencies # next vertex / weight