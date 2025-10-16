from enum import Enum
class Node():
    def __init__(self, newID: int, adjascencies: dict):
        self.nodeID: int = newID
        self.adjascentVertices: dict = adjascencies # next vertex / weight
    
    def setAdjascencies(self, newAdjascencies: dict):
        self.adjascentVertices = newAdjascencies
    
    def __str__(self):
        returnStr: str = ""
        returnStr += f"Node {self.nodeID} information\n"
        returnStr += f"Vertices: {self.adjascentVertices}\n"
        return returnStr