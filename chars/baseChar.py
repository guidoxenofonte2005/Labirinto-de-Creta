# Importa as classes Node e Graph, necessárias para representar o labirinto
from objects.node import Node
from objects.graph import Graph
import random

class BaseChar():
    """Define a estrutura mínima de qualquer personagem:
    - Ele tem uma posição (um vértice do grafo)
    - E pode se mover para um vértice adjacente"""

    def __init__(self, initialPos: Node):
        """Inicializa o personagem em uma posição específica do grafo, onde o personagem começa o jogo."""
        self.position: Node = initialPos  # Armazena o nó atual onde o personagem está


    def move(self, currentNode: Node, graph: Graph) -> None:
        """Move o personagem para um vértice aleatório adjacente.
             currentNode: nó atual onde o personagem está
             graph: estrutura do labirinto (grafo)"""
        
        
        # Obtém todos os vértices vizinhos (adjacentes) do nó atual.
        nodes: list = list(currentNode.adjascentVertices.keys())

        """Escolhe aleatoriamente um dos vértices adjacentes, definindo o próximo movimento do personagem"""
        selectedNode = int(random.choice(nodes))

        #Atualiza a posição do personagem para o novo vértice escolhido.
        self.position = graph.vertices[selectedNode]
