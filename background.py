import random

class Tree():

    def __init__(self):
        self.tre = [
            [' ',' ','/','\\',' ',' '],
            [' ','/',' ',' ','\\',' '],
            ['/','_',' ',' ','_','\\'],
            [' ','/',' ',' ','\\',' '],
            ['/','_','_','_','_','\\'],
            ['_','_','|','|','_','_']
        ]

        self.pos_x = 12
        self.pos_y = random.randint(10, 380)

    def draw(self, box, org):
        for i in range(len(self.tre)):
            for j in range(len(self.tre[i])):
                box[self.pos_x + i][org[0] + self.pos_y + j] = self.tre[i][j]

    def __str__(self):
        return str(self.pos_x) + ',' + str(self.pos_y)

class Cloud():

    def __init__(self):
        self.str = [
            [' ', ' ', ' ', '_', '_', ' ', ' ', ' '],
            [' ', '_', '(', ' ', ' ', ')', '_', ' '],
            ['(', '_', ' ', '_', ' ', '_', ' ', ')']
        ]

        self.pos_x = random.randint(5, 10)
        self.pos_y = random.randint(0, 360)
    
    def draw(self, box, org):
        for i in range(len(self.str)):
            for j in range(len(self.str[i])):
                box[self.pos_x + i][org[0] + self.pos_y + j] = self.str[i][j]
    
    def __str__(self):
        return str(self.pos_x) + ',' + str(self.pos_y)
