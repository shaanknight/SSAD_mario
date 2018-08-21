def paintempty(self, box, org):
    for i in range(2):
        for j in range(2):
            box[self.pos[0] + i][org[0] + self.pos[1] + j] = ' '

def paintfill(self, box, org):
    for i in range(2):
        for j in range(2):
            box[self.pos[0] + i][org[0] + self.pos[1] + j] = self.str[i][j]
