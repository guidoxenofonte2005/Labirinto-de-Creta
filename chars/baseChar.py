import random
from objects.node import Node

class BaseChar():
    def __init__(self, initialPos: int):
        self.position: int = initialPos
    
    def move(self, currentNode: Node, speed: int = 1) -> None:
        for _ in range(speed):
            self.position = random.choice(list(currentNode.adjascentVertices.keys()))