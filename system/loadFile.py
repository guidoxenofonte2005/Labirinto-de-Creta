import json

class LoadFileSystem:
    def __init__(self, fileLocation: str):
        try:
            with open(fileLocation, 'r') as file:
                self.content: dict = json.load(file)
        except FileNotFoundError as e:
            print("Error, file not found")
            self.content = None
        # print(self.content.values())
    