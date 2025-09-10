from chars.baseChar import *
from objects.node import Node

from random import randint

class Minotaur(BaseChar):
    def __init__(self, initialPos: int, detectionDistance: int):
        super().__init__(initialPos)
        self.detectionDistante = detectionDistance
        self.DETECTED_PLAYER = False
        self.pursuitOrderArray: list[Node] = []

    def characterCheck(self, minDistanceToPlayer: int):
        self.DETECTED_PLAYER = minDistanceToPlayer <= self.detectionDistante

    def combat(self) -> bool:
        return randint(1, 100) == 1