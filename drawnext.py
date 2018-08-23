''' utility functions to remove from the board the previous mario position and add to the board current mario position '''

def paintempty(self, box, org):
    for i in range(len(self.str)):
        for j in range(len(self.str[i])):
            box[self.pos[0] + i][org[0] + self.pos[1] + j] = ' '

def paintfill(self, box, vir,org):
    for i in range(len(self.str)):
        for j in range(len(self.str[i])):
            box[self.pos[0] + i][org[0] + self.pos[1] + j] = self.str[i][j]
            vir[self.pos[0] + i][org[0] + self.pos[1] + j] = 1


