from objects.graph import Graph
from system.loadFile import *

from chars.minotaur import *
from chars.labyrinthGuy import *


class Main:
    def __init__(self, fileLocation: str = "graph.json"):
        loadSys = LoadFileSystem(fileLocation)

        self.graph: Graph = Graph(loadSys.content["enterVertex"], loadSys.content["exitVertex"], loadSys.content["numVertices"])
        self.graph.setNodeInfo(loadSys.content["edgeList"])

        self.minotaur = Minotaur(self.graph.vertices[loadSys.content["minotaurInitialPos"]], loadSys.content["minotaurDetectionDistance"])
        self.labyrinthGuy = LabyrinthGuy(self.graph.vertices[loadSys.content["enterVertex"]], loadSys.content["foodTime"])

        self.iterationCounter: int = 0

    def runIteration(self) -> int:
        """
        1 - mover entrante\n
        2 - mover minotauro\n
        3 - checar saída no entrante\n
        4 - checar detecção no minotauro\n
        5 - checar se ambos estão no mesmo lugar\n
        6 - processar batalha\n
        7 - diminuir suprimentos\n
        """
        

        self.labyrinthGuy.supplies -= 1 #Movi pra cá pra garantir que o suprimento diminua mesmo se o entrante não se mover
        self.iterationCounter += 1
        self.labyrinthGuy.move(self.graph)
        if self.labyrinthGuy.isExitFound(self.graph.vertices[self.graph.end]):
            return 1
        self.minotaur.characterCheck(self.graph.findNode(self.minotaur.position, self.labyrinthGuy.position))
        self.minotaur.move(self.minotaur.position, self.graph, self.labyrinthGuy.position)
        if self.minotaur.position == self.labyrinthGuy.position:
            if not self.minotaur.combat():
                return -1
        if self.labyrinthGuy.supplies <= 0:
            return -2
        return 0

main = Main()
codeResult = 0
while (codeResult == 0):
    codeResult = main.runIteration()

# Teste print:
main = Main()
codeResult = 0

# imprime o estado inicial antes do loop começar
print(f"Início da Simulação: Entrante no nó {main.labyrinthGuy.position.nodeID}, Minotauro no nó {main.minotaur.position.nodeID}")
print("-" * 40) 

while (codeResult == 0):
    # Guarda a posição anterior para ver o movimento 
    posicao_anterior = main.labyrinthGuy.position.nodeID

    codeResult = main.runIteration()

    # Bloco de impressões a cada iteração para depuração
    print(f"Iteração: {main.iterationCounter}")
    print(f"  - Posição do Entrante: {posicao_anterior} -> {main.labyrinthGuy.position.nodeID}")
    
    # Converte a lista de nós para uma lista de IDs para facilitar a leitura
    caminho_percorrido = [node.nodeID for node in main.labyrinthGuy.yarnThread]
    print(f"  - Fio de Lã (Pilha): {caminho_percorrido}")
    print(f"  - Suprimentos restantes: {main.labyrinthGuy.supplies}")
    print("-" * 40)


print(f"fim do programa: código {codeResult, main.iterationCounter}")