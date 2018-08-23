from random import randint,choice

''' tree class '''

class Tree():

    def __init__(self):
        self.tre = [
            [' ',' ','\033[1;32m/\033[0m','\033[1;32m\\\033[0m',' ',' '],
            [' ','\033[1;32m/\033[0m',' ',' ','\033[1;32m\\\033[0m',' '],
            ['\033[1;32m/\033[0m','\033[1;32m_\033[0m',' ',' ','\033[1;32m_\033[0m','\033[1;32m\\\033[0m'],
            [' ','\033[1;32m/\033[0m',' ',' ','\033[1;32m\\\033[0m',' '],
            ['\033[1;32m/\033[0m','\033[1;32m_\033[0m','\033[1;32m_\033[0m','\033[1;32m_\033[0m','\033[1;32m_\033[0m','\033[1;32m\\\033[0m'],
            ['\033[1;32m_\033[0m','\033[1;32m_\033[0m','\033[1;32m|\033[0m','\033[1;32m|\033[0m','\033[1;32m_\033[0m','\033[1;32m_\033[0m']
        ]

        self.pos_x = 12
        self.pos_y = choice([randint(10, 110),randint(130,350)])

    def draw(self, box, org):
        for i in range(len(self.tre)):
            for j in range(len(self.tre[i])):
                box[self.pos_x + i][org[0] + self.pos_y + j] = self.tre[i][j]

    def __str__(self):
        return str(self.pos_x) + ',' + str(self.pos_y)

''' cloud class '''

class Cloud():

    def __init__(self):
        self.str = [
            [' ', ' ', ' ', '\033[1;34m_\033[0m', '\033[1;34m_\033[0m', ' ', ' ', ' '],
            [' ', '\033[1;34m_\033[0m', '\033[1;34m(\033[0m', ' ', ' ', '\033[1;34m)\033[0m', '\033[1;34m_\033[0m', ' '],
            ['\033[1;34m(\033[0m', '\033[1;34m_\033[0m', ' ', '\033[1;34m_\033[0m', ' ', '\033[1;34m_\033[0m', ' ', '\033[1;34m)\033[0m']
        ]

        self.pos_x = randint(5, 10)
        self.pos_y = choice([randint(10, 110),randint(130,350)])
    
    def draw(self, box, org):
        for i in range(len(self.str)):
            for j in range(len(self.str[i])):
                box[self.pos_x + i][org[0] + self.pos_y + j] = self.str[i][j]
    
    def __str__(self):
        return str(self.pos_x) + ',' + str(self.pos_y)

''' level 2 display class '''

class show2():

    def __init__(self):
        self.str = [
            ['L','E','V','E','L',':','2']
        ]

        self.pos_x = 7
        self.pos_y = 117
    
    def draw(self, box, org):
        for i in range(len(self.str)):
            for j in range(len(self.str[i])):
                box[self.pos_x + i][org[0] + self.pos_y + j] = self.str[i][j]
    
    def __str__(self):
        return str(self.pos_x) + ',' + str(self.pos_y)

''' level 1 display class '''

class show1():

    def __init__(self):
        self.str = [
            ['L','E','V','E','L',':','1']
        ]

        self.pos_x = 7
        self.pos_y = 3
    
    def draw(self, box, org):
        for i in range(len(self.str)):
            for j in range(len(self.str[i])):
                box[self.pos_x + i][org[0] + self.pos_y + j] = self.str[i][j]
    
    def __str__(self):
        return str(self.pos_x) + ',' + str(self.pos_y)


