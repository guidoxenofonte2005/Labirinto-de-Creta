from chars.baseChar import *
from objects.node import Node
from objects.graph import Graph
from random import randint, choice

class Minotaur(BaseChar):
    def __init__(self, initialPos: Node, detectionDistance: int):
        super().__init__(initialPos)
        self.detectionDistante = detectionDistance
        self.DETECTED_PLAYER = False
        # Lista para guardar os IDs (int) dos nós percorridos durante a perseguição
        self.pursuit_path: list[int] = []
        # Lista para guardar o histórico completo de movimentos.
        self.path_history: list[int] = [initialPos.nodeID]

    def characterCheck(self, minDistanceToPlayer: int) -> bool:
        # Verifica se o jogador foi detectado. Retorna True apenas na primeira vez.
        
        # Se o jogador já foi detectado antes, não há mudança de estado.
        if self.DETECTED_PLAYER:
            return False
            
        # Verifica se a distância atual ativa a detecção.
        if minDistanceToPlayer <= self.detectionDistante:
            self.DETECTED_PLAYER = True
            return True  # Retorna True para sinalizar que a detecção ACABOU de ocorrer.
            
        return False

    def combat(self) -> bool:
        # Retorna True se o prisioneiro vencer o combate (chane baixa).
        return randint(1, 100) == 1
    
    def move(self, currentNode: Node, graph: Graph, chaseNode: Node = None):
        """
        Move o Minotauro:
        - 1 passo aleatório se não estiver em modo de perseguição.
        - Até 2 passos pelo caminho mínimo em direção ao jogador se estiver perseguindo.
        """

        # Se não detectou o jogador, move-se 1 passo aleatório.
        if not self.DETECTED_PLAYER or chaseNode is None:
            # Reutiliza a lógica de movimento aleatório da classe pai (BaseChar)
            super().move(currentNode, graph)
            self.path_history.append(self.position.nodeID)
            return

        # Se a perseguição acabou de começar, adiciona a posição inicial ao caminho.
        if not self.pursuit_path:
            self.pursuit_path.append(currentNode.nodeID)
            
        # Pede ao grafo que calcule o caminho mínimo.
        path = graph.findPath(currentNode, chaseNode)
        
        # Se houver um caminho válido...
        if path and len(path) > 1:
            # Determina quantos passos dar (no máximo 2).
            steps_to_move = min(len(path) - 1, 2)

            # Guarda a posição antiga antes de mover.
            old_position_id = self.position.nodeID
            
            # Atualiza a posição para o destino final desta rodada.
            self.position = path[steps_to_move]
            
            # Adiciona os nós percorridos (passos intermediários) ao registro do caminho.
            for i in range(1, steps_to_move + 1):
                self.pursuit_path.append(path[i].nodeID)

            if self.position.nodeID != old_position_id:
                self.path_history.append(self.position.nodeID)
        else:
            # Se não houver caminho (raro), move-se aleatoriamente para não ficar parado.
            super().move(currentNode, graph)
            self.path_history.append(self.position.nodeID)