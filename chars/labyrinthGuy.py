import random

from chars.baseChar import *
from objects.node import Node
from objects.graph import Graph

class LabyrinthGuy(BaseChar):
    def __init__(self, initialPos: Node, supplyAmount: int):
        super().__init__(initialPos)

        #A pilha yarnThread agora guarda o caminho percorrido pelo personagem

        self.yarnThread: list[Node] = [initialPos] #pilha 
        self.supplies: int = supplyAmount
    
    def move(self, graph:Graph):
        currentNode = self.position
        adjacent_nodes = list(currentNode.adjascentVertices.keys())

        # Filtra os nós adjacentes que não foram visitados.
        unvisited_nodes = [ node for node in adjacent_nodes if graph.vertices[int(node)] not in self.yarnThread]

        #DFS para exploração do labirinto
        if unvisited_nodes:
            #seleciona um nó não visitado aleatoriamente
            selectedNodeId = int(random.choice(unvisited_nodes))
            nextNode = graph.vertices[selectedNodeId]

            #atualiza posição e pilha adicionando o novo nó.
            self.position = nextNode
            self.yarnThread.append(nextNode)

        else:
            #se todos os nós adjacentes já foram visitados
            if len(self.yarnThread) > 1:
                self.yarnThread.pop() #remove o nó atual pra voltar pro nó anterior
                self.position = self.yarnThread[-1] #atualiza a posição para o nó anterior (novo topo)
        


    def isExitFound(self, exitPosition: Node) -> bool:
        return self.position.nodeID == exitPosition.nodeID