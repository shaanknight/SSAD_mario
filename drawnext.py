def paintempty(self,box):
    for i in range(2):
        for j in range(2):
            box[self.pos[0] + i][self.pos[1] + j] = ' '

def paintfill(self,box):
    for i in range(2):
        for j in range(2):
            box[self.pos[0] + i][self.pos[1] + j] = self.str[i][j]
