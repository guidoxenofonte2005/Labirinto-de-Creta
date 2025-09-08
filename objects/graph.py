from chars.minotaur import *

class Node():
    def __init__(self, newID: int, adjascencies: list[tuple[int, int]]):
        self.nodeID: int = newID
        self.adjascentVertices: list[tuple[int, int]] = adjascencies

    def __str__(self):
        pass


class Graph():
    def __init__(self, labyrinthStart: int, labyrinthEnd: int, startMinotaurPos: int):
        self.vertices: list[Node] = []
        self.minotaur: Minotaur = Minotaur(startMinotaurPos)
        self.start = labyrinthStart
        self.end = labyrinthEnd

    def runIteration(self) -> None:
        """
        1 - mover entrante\n
        2 - mover minotauro\n
        3 - checar saída no entrante\n
        4 - checar detecção no minotauro\n
        5 - checar se ambos estão no mesmo lugar\n
        6 - processar batalha\n
        7 - diminuir suprimentos\n
        """
        pass

    def findNode(self, startNode: int, searchedNode: int) -> int:
        pass