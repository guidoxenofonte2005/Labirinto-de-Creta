from objects.graph import Graph
from system.loadFile import *
from chars.minotaur import *
from chars.labyrinthGuy import *
import time
import random 

class Main:
    def __init__(self, fileLocation: str = "graph.json"):
        loadSys = LoadFileSystem(fileLocation)
        self.graph = Graph(loadSys.content["enterVertex"], loadSys.content["exitVertex"], loadSys.content["numVertices"])
        self.graph.setNodeInfo(loadSys.content["edgeList"])

        
        # Cria o Minotauro na posição inicial informada no arquivo e define a distância máxima de detecção
        self.minotaur = Minotaur(self.graph.vertices[loadSys.content["minotaurInitialPos"]], loadSys.content["minotaurDetectionDistance"])

        self.labyrinthGuy = LabyrinthGuy(self.graph.vertices[loadSys.content["enterVertex"]], loadSys.content["foodTime"])
        
        self.iterationCounter: int = 0
        self.detection_iteration = None
        self.capture_iteration = None
        self.final_code = 0

        excluded = {self.graph.start, self.graph.end, self.minotaur.position.nodeID}
        possible_nodes = [i for i in range(len(self.graph.vertices)) if i not in excluded]
        self.map_node = random.choice(possible_nodes)

    def show_map_path(self):
        print("\n--- O MAPA REVELA O CAMINHO ---")
        
        start_node = self.labyrinthGuy.position
        exit_node = self.graph.vertices[self.graph.end]
        shortest_path_nodes = self.graph.findPath(start_node, exit_node)
        
        if shortest_path_nodes:
            shortest_path_ids = [node.nodeID for node in shortest_path_nodes]
            path_range = shortest_path_ids[:8]
            
            print(f"O mapa revela os próximos {len(path_range) - 1} passos do caminho mais curto:")
            print(f"==> {path_range}")
        else:
            print("Não foi possível calcular um caminho para a saída a partir daqui.")

        print("--------------------------------\n")
        time.sleep(3)

    def runIteration(self) -> int:
        self.iterationCounter += 1
        
        exit_node = self.graph.vertices[self.graph.end]
        self.labyrinthGuy.move(self.graph, exit_node)

        if self.labyrinthGuy.position.nodeID == self.map_node:
            if not self.labyrinthGuy.has_map:
                self.labyrinthGuy.has_map = True
                self.labyrinthGuy.map_duration = 7
                print(f"🗺️  O entrante encontrou um mapa! Ele pode fazer {self.labyrinthGuy.map_duration} movimentos inteligentes.")
                self.show_map_path()
        
        if self.labyrinthGuy.isExitFound(exit_node):
            self.final_code = 1
            return 1

        # Usa Dijkstra para calcular a distância entre o Minotauro e o Entrante
        distance = self.graph.findNode(self.minotaur.position, self.labyrinthGuy.position)

        """ Se o jogador estiver dentro do raio de percepção p(G),
        o método characterCheck() muda o estado DETECTED_PLAYER para True.
        A primeira vez que isso acontece é registrada para o relatório"""
        if self.minotaur.characterCheck(distance) and self.detection_iteration is None:
            self.detection_iteration = self.iterationCounter

        """O método move() controla tanto o movimento aleatório (antes da detecção)
        quanto o movimento de perseguição(depois a detecção)"""
        self.minotaur.move(self.minotaur.position, self.graph, self.labyrinthGuy.position)


        # Se o Minotauro e o Entrante estão no mesmo nó, inicia combate.
        if self.minotaur.position.nodeID == self.labyrinthGuy.position.nodeID:
            self.capture_iteration = self.iterationCounter
            # Método combat(): 1% chance do jogador vencer
            if not self.minotaur.combat():
                self.final_code = -1 #Jogador morreu
                return -1
            else:
                self.final_code = 2 #Jogador venceu
                return 2

        self.labyrinthGuy.supplies -= 1
        if self.labyrinthGuy.supplies <= 0:
            self.final_code = -2
            return -2
            
        return 0

main = Main()
codeResult = 0

print("=============================================")
print("INÍCIO DA SIMULAÇÃO")
print("=============================================")
print(f"Localização do Mapa Secreto: Nó {main.map_node}")
print(f"Entrante começa no nó: {main.labyrinthGuy.position.nodeID}")
print(f"Minotauro começa no nó: {main.minotaur.position.nodeID}")
print(f"Suprimentos iniciais: {main.labyrinthGuy.supplies}")
print("---------------------------------------------")
time.sleep(2)

while codeResult == 0:
    posicao_anterior_guy = main.labyrinthGuy.position.nodeID
    posicao_anterior_minotaur = main.minotaur.position.nodeID
    codeResult = main.runIteration()
    print(f"Rodada: {main.iterationCounter}")
    print(f"  - Entrante moveu: {posicao_anterior_guy} -> {main.labyrinthGuy.position.nodeID}")
    print(f"  - Minotauro moveu: {posicao_anterior_minotaur} -> {main.minotaur.position.nodeID}")
    caminho_entrante_ids = [node.nodeID for node in main.labyrinthGuy.yarnThread]
    print(f"  - Fio de Lã (Caminho do Entrante): {caminho_entrante_ids}")

    # Mostra caminho percorrido pelo Minotauro durante toda a simulação
    if hasattr(main.minotaur, 'path_history'):
        print(f"  - Caminho do Minotauro: {main.minotaur.path_history}")
        
    # Mostra detalhes do caminho apenas durante perseguição
    if main.minotaur.pursuit_path:
        print(f"  - (Detalhe Perseguição): {main.minotaur.pursuit_path}")
    print(f"  - Suprimentos restantes: {main.labyrinthGuy.supplies}")
    print(f"  - Minotauro detectou o jogador: {main.minotaur.DETECTED_PLAYER}")
    print("---------------------------------------------")
    time.sleep(0.5)

print("\n=============================================")
print("FIM DA SIMULAÇÃO")
print("=============================================")
if codeResult == 1:
    print("VITÓRIA: O prisioneiro encontrou a saída!")
elif codeResult == 2:
    print("VITÓRIA: O prisioneiro derrotou o Minotauro em combate!")
elif codeResult == -1:
    print("DERROTA: O prisioneiro foi pego e morto pelo Minotauro.")
elif codeResult == -2:
    print("DERROTA: O prisioneiro ficou sem suprimentos e morreu.")
print(f"Resultado final: código {codeResult} (após {main.iterationCounter} rodadas)")
print("=============================================")