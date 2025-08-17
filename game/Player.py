class Player:
    def __init__(self,inventory,description):
        self.description = description
        self.inventory = inventory

    def __str__(self):
        return f'{self.description}'

    def showInventory(self):
        return self.inventory