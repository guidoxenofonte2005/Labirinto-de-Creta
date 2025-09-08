from baseChar import BaseChar

class LabyrinthGuy(BaseChar):
    def __init__(self, initialPos: int):
        super().__init__(initialPos)
    
    def isExitFound(self, exitPosition: int) -> bool:
        return self.position == exitPosition