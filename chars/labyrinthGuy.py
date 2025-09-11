import random

from chars.baseChar import *
from objects.node import Node

class LabyrinthGuy(BaseChar):
    def __init__(self, initialPos: Node, supplyAmount: int):
        super().__init__(initialPos)
        self.yarnThread: list[Node] = []
        self.supplies: int = supplyAmount
    
    def isExitFound(self, exitPosition: int) -> bool:
        return self.position == exitPosition
    
    def move(self, currentNode: Node):
        return super().move(currentNode)