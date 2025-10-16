from chars.baseChar import *   
from objects.node import Node  # Importa o node e graph que estão relacionados a o lairinto
from objects.graph import Graph
from random import randint, choice

class Minotaur(BaseChar):
    def __init__(self, initialPos: Node, detectionDistance: int):
        # Chama o construtor da classe base para definir posição inicial
        super().__init__(initialPos)

        # Raio de detecção do jogador (número de nós de distância)
        self.detectionDistance = detectionDistance

        # Indica se o jogador já foi detectado (modo perseguição ativo)
        self.DETECTED_PLAYER = False

        # Caminho da perseguição: armazena os nós desde que começou a perseguir
        self.pursuit_path: list[int] = []

        # Caminho total: histórico de todos os nós visitados
        self.path_history: list[int] = [initialPos.nodeID]

    def characterCheck(self, minDistanceToPlayer: int) -> bool:
        """Verifica se o jogador está dentro da distância de detecção.
        Retorna True apenas na primeira vez que o jogador é detectado."""

        if self.DETECTED_PLAYER:
            # Já estava perseguindo, não faz nada
            return False

        # Se o jogador estiver dentro do raio de detecção, ativa perseguição
        if minDistanceToPlayer <= self.detectionDistance:
            self.DETECTED_PLAYER = True
            return True

        return False

    def combat(self) -> bool:
        """Simula uma batalha entre o jogador e o Minotauro.
        Retorna True se o jogador vencer (1% de chance)."""
        return randint(1, 100) == 1

    def move(self, currentNode: Node, graph: Graph, chaseNode: Node = None):
        """Move o Minotauro:
        - Movimento aleatório se não estiver perseguindo
        - Caminho controlado (até 2 nós por rodada) se estiver perseguindo o jogador"""

        # Minotauro ainda não detectou o jogador, move apenas 1 nó aleatoriamente
        if not self.DETECTED_PLAYER or chaseNode is None:
            # Move aleatoriamente (função herdada da classe baseChar)
            super().move(currentNode, graph)

            # Adiciona o novo nó ao histórico completo
            if self.path_history[-1] != self.position.nodeID:
                self.path_history.append(self.position.nodeID)
            return


        # Minotauro detectou o jogador (modo perseguição)
        # Se é o primeiro turno da perseguição, registra o nó inicial
        if not self.pursuit_path:
            self.pursuit_path.append(currentNode.nodeID)

        # Encontra o caminho mínimo até o jogador
        path = graph.findPath(currentNode, chaseNode)

        if path and len(path) > 1:
            # Pode andar até 2 nós por rodada
            steps_to_move = min(len(path) - 1, 2)

            # Percorre os nós do caminho
            for i in range(1, steps_to_move + 1):
                node = path[i]
                self.position = node  # atualiza posição

                # Registra o nó na lista de perseguição
                if self.pursuit_path[-1] != node.nodeID:
                    self.pursuit_path.append(node.nodeID)

                # Registra também no histórico total
                if self.path_history[-1] != node.nodeID:
                    self.path_history.append(node.nodeID)

        else:
            # Caso o grafo não encontre caminho, move aleatoriamente
            super().move(currentNode, graph)

            #Sempre atualiza o histórico completo
            if self.path_history[-1] != self.position.nodeID:
                self.path_history.append(self.position.nodeID)

            #atualiza o detalhe da perseguição já que o modo perseguição continua ativo
            if self.pursuit_path[-1] != self.position.nodeID:
                self.pursuit_path.append(self.position.nodeID)
