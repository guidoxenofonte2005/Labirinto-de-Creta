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

        self.has_map = False
        self.map_duration = 0
    
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
    
        # Método principal que decide qual estratégia de movimento usar.
        
        # Se o jogador tem o mapa e o seu efeito ainda está ativo...
        if self.has_map and self.map_duration > 0:
            # usa o movimento inteligente (guloso).
            self.move_greedy(graph, exitNode)
            # Decrementa a duração do mapa após o movimento.
            self.map_duration -= 1
            # Se a duração acabou, informa o jogador.
            if self.map_duration == 0:
                print("🗺️ O efeito do mapa terminou! O entrante volta a explorar por conta própria.")
        else:
            # Caso contrário, usa a exploração normal (DFS).
            self.move_dfs(graph)

    def move_dfs(self, graph: Graph):
        """
        Move o jogador usando a exploração DFS,
        o seu comportamento padrão sem o mapa.
        """
        currentNode = self.position
        adjacent_nodes = list(currentNode.adjascentVertices.keys())

        # Filtra os nós adjacentes que não foram visitados.
        unvisited_nodes = [node for node in adjacent_nodes if graph.vertices[int(node)] not in self.yarnThread]

        # Se houver vizinhos não visitados, avança.
        if unvisited_nodes:
            selectedNodeId = int(random.choice(unvisited_nodes))
            nextNode = graph.vertices[selectedNodeId]
            self.position = nextNode
            self.yarnThread.append(nextNode)
        # Se não houver, retrocede (backtracking).
        else:
            if len(self.yarnThread) > 1:
                self.yarnThread.pop() # Remove o nó atual do "fio de lã".
                self.position = self.yarnThread[-1] # Volta para a posição anterior.

    def move_greedy(self, graph: Graph, exitNode: Node):
        
        # Faz o uso de Dijkstra (através do graph.findNode).
        
        currentNode = self.position
        adjacent_nodes = list(currentNode.adjascentVertices.keys())

        if not adjacent_nodes:
            return

        best_neighbor = None
        min_distance_to_exit = float('inf')

        # Itera sobre cada vizinho para encontrar o melhor passo.
        for neighbor_id_str in adjacent_nodes:
            neighbor_node = graph.vertices[int(neighbor_id_str)]
            # Usa Dijkstra para calcular a distância do vizinho até à saída.
            distance = graph.findNode(neighbor_node, exitNode)
            if distance < min_distance_to_exit:
                min_distance_to_exit = distance
                best_neighbor = neighbor_node
        
        # Move-se para o melhor vizinho encontrado.
        if best_neighbor:
            self.position = best_neighbor
            self.yarnThread.append(self.position)

    def isExitFound(self, exitPosition: Node) -> bool:
        return self.position.nodeID == exitPosition.nodeID