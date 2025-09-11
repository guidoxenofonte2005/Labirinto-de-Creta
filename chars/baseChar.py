import random

from objects.node import Node
from objects.graph import Graph

class BaseChar():
    def __init__(self, initialPos: Node):
        self.position: Node = initialPos
    
    def move(self, currentNode: Node, graph: Graph) -> None:
        nodes: list = list(currentNode.adjascentVertices.keys())
        selectedNode = int(random.choice(nodes))

        self.position = graph.vertices[selectedNode]