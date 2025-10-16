import random

from chars.baseChar import *
from objects.node import Node
from objects.graph import Graph

class LabyrinthGuy(BaseChar):
    def __init__(self, initialPos: Node, supplyAmount: int):
        super().__init__(initialPos)
        self.yarnThread: list[Node] = [initialPos] #pilha 
        self.supplies: int = supplyAmount
        self.has_map = False
        self.map_duration = 0
    
    def move(self, graph: Graph, exitNode: Node):
        if self.has_map and self.map_duration > 0:
            self.move_greedy(graph, exitNode)
            self.map_duration -= 1
            if self.map_duration == 0:
                print("🗺️ O efeito do mapa terminou! O entrante volta a explorar por conta própria.")
        else:
            self.move_dfs(graph)

    def move_dfs(self, graph: Graph):
        
        currentNode = self.position
        adjacent_nodes = list(currentNode.adjascentVertices.keys())

        unvisited_nodes = [node for node in adjacent_nodes if graph.vertices[int(node)] not in self.yarnThread]

        if unvisited_nodes:
            selectedNodeId = int(random.choice(unvisited_nodes))
            nextNode = graph.vertices[selectedNodeId]
            self.position = nextNode
            self.yarnThread.append(nextNode)
        
        else:
            if len(self.yarnThread) > 1:
                self.yarnThread.pop() 
                self.position = self.yarnThread[-1] 

    def move_greedy(self, graph: Graph, exitNode: Node):
        currentNode = self.position
        adjacent_nodes = list(currentNode.adjascentVertices.keys())

        if not adjacent_nodes:
            return

        best_neighbor = None
        min_distance_to_exit = float('inf')

        for neighbor_id_str in adjacent_nodes:
            neighbor_node = graph.vertices[int(neighbor_id_str)]
            distance = graph.findNode(neighbor_node, exitNode)
            if distance < min_distance_to_exit:
                min_distance_to_exit = distance
                best_neighbor = neighbor_node
    
        if best_neighbor:
            self.position = best_neighbor
            self.yarnThread.append(self.position)

    def isExitFound(self, exitPosition: Node) -> bool:
        return self.position.nodeID == exitPosition.nodeID