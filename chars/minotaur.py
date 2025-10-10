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

        """Move o Minotauro de acordo com o modo atual (normal ou perseguição)
        Parâmetros
        currentNode (Node): nó atual do Minotauro
        graph (Graph): grafo do labirinto
        chaseNode (Node, opcional): nó do jogador (usado para perseguição)"""

        # Se o Minotauro nao esta perseguindo ou nao foi passado o no do jogador
        if not self.DETECTEDPLAYER or chaseNode is None:
            #Obtém a lista de vértices adjacentes ao nó atual.
            adjacentes = list(currentNode.adjascentVertices.keys())
            if adjacentes:
                #Escolhe um vértice aleatório entre os adjacentes para seguir caminho
                self.position = graph.vertices[adjacentes[randint(0, len(adjacentes) - 1)]]

        else:
            #Se esta perseguindo, calcula o caminho mínimo até o jogador
            path = graph.findPath(currentNode, chaseNode)
            #Se o caminho tem pelo menos 3 nós, pode andar 2 vértices.
            if path is not None and len(path) > 2:
                self.position = graph.vertices[path[2]]#Move dois vértices pelo caminho mínimo

            # Se o caminho tem só 2 nós, anda apenas 1 vértice (posição = segundo nó do caminho)
            elif path is not None and len(path) > 1:
                self.position = graph.vertices[path[1]]# Se já está no mesmo nó do o jogador, não move