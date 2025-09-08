from baseChar import BaseChar
from objects.graph import Node

class Minotaur(BaseChar):
    def __init__(self, initialPos: int, detectionDistance: int):
        super().__init__(initialPos)
        self.detectionDistante = detectionDistance
        self.DETECTED_PLAYER = False
        self.pursuitOrderArray: list[Node] = []

    def characterCheck(self, labyrinthGuyPos: int):
        pass

    def combat(self):
        pass