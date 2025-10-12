from objects.graph import Graph
from system.loadFile import *
from chars.minotaur import *
from chars.labyrinthGuy import *
import time

class Main:
    def __init__(self, fileLocation: str = "graph.json"):
        # Inicializa a simulação carregando todas as configurações do arquivo
        loadSys = LoadFileSystem(fileLocation)
        self.graph = Graph(loadSys.content["enterVertex"], loadSys.content["exitVertex"], loadSys.content["numVertices"])
        self.graph.setNodeInfo(loadSys.content["edgeList"])
        self.minotaur = Minotaur(self.graph.vertices[loadSys.content["minotaurInitialPos"]], loadSys.content["minotaurDetectionDistance"])
        self.labyrinthGuy = LabyrinthGuy(self.graph.vertices[loadSys.content["enterVertex"]], loadSys.content["foodTime"])
        
        self.iterationCounter: int = 0
        # Variáveis para registrar eventos importantes para o relatório
        self.detection_iteration = None
        self.capture_iteration = None
        self.final_code = 0

    def runIteration(self) -> int:
        # Executa uma única rodada (iteração) da simulação
        self.iterationCounter += 1
        
        # 1. Mover o entrante (LabyrinthGuy)
        self.labyrinthGuy.move(self.graph)
        
        # 2. Verificar se o entrante encontrou a saída
        exit_node = self.graph.vertices[self.graph.end] # Procura no graph.json o vétcie que foi definida a saída e utiliza para verificar se saiu ou n
        if self.labyrinthGuy.isExitFound(exit_node):
            self.final_code = 1
            return 1

        # 3. Verificar a distância e o estado de detecção do Minotauro
        distance = self.graph.findNode(self.minotaur.position, self.labyrinthGuy.position) # Verifica a distância entre o minotauro e o player
        if self.minotaur.characterCheck(distance) and self.detection_iteration is None: # Vê se a distância entre minotauro e player é igual a distância de detecção 
            self.detection_iteration = self.iterationCounter

        # 4. Mover o Minotauro
        self.minotaur.move(self.minotaur.position, self.graph, self.labyrinthGuy.position)
        
        # 5. Verificar se houve encontro para iniciar combate
        if self.minotaur.position.nodeID == self.labyrinthGuy.position.nodeID:
            self.capture_iteration = self.iterationCounter
            if not self.minotaur.combat():
                self.final_code = -1 # Derrota em combate
                return -1
            else:
                self.final_code = 2 # Vitória em combate (raro)
                return 2

        # 6. Consumir suprimentos
        self.labyrinthGuy.supplies -= 1
        if self.labyrinthGuy.supplies <= 0:
            self.final_code = -2 # Derrota por fome
            return -2
            
        return 0 # Jogo continua

# A patir daqui vai ser o vloco de exec principal
main = Main()
codeResult = 0

# Imprime o cabeçalho inicial da simulação
print("=============================================")
print("INÍCIO DA SIMULAÇÃO")
print("=============================================")
print(f"Entrante começa no nó: {main.labyrinthGuy.position.nodeID}")
print(f"Minotauro começa no nó: {main.minotaur.position.nodeID}")
print(f"Suprimentos iniciais: {main.labyrinthGuy.supplies}")
print("---------------------------------------------")
time.sleep(2) # Pausa para o usuário ler as informações iniciais

# Loop principal da simulação
while codeResult == 0:
    # Armazena as posições antes do movimento para o relatório da rodada
    posicao_anterior_guy = main.labyrinthGuy.position.nodeID
    posicao_anterior_minotaur = main.minotaur.position.nodeID

    codeResult = main.runIteration()

    # Imprime o relatório da rodada no formato solicitado
    print(f"Rodada: {main.iterationCounter}")
    print(f"  - Entrante moveu: {posicao_anterior_guy} -> {main.labyrinthGuy.position.nodeID}")
    print(f"  - Minotauro moveu: {posicao_anterior_minotaur} -> {main.minotaur.position.nodeID}")
    
    caminho_entrante_ids = [node.nodeID for node in main.labyrinthGuy.yarnThread]
    print(f"  - Fio de Lã (Caminho do Entrante): {caminho_entrante_ids}")
    
    # Exibe o caminho de perseguição do Minotauro apenas se ele tiver começado
    if main.minotaur.pursuit_path:
        print(f"  - Caminho de Perseguição do Minotauro: {main.minotaur.pursuit_path}")

    print(f"  - Suprimentos restantes: {main.labyrinthGuy.supplies}")
    print(f"  - Minotauro detectou o jogador: {main.minotaur.DETECTED_PLAYER}")
    print("---------------------------------------------")
    
    time.sleep(0.5) # Pausa entre as rodadas para facilitar a visualização

# Imprime o rodapé com o resultado final da simulação
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
