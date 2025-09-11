import random
from objects.node import Node

class BaseChar():
    def __init__(self, initialPos: Node):
        self.position: Node = initialPos
    
    def move(self, currentNode: Node) -> None:
        self.position = random.choice(list(currentNode.adjascentVertices.keys()))