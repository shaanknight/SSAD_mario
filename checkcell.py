def checkh(self, vir, org, rem):
	if (vir[self.pos[0]][org[0] + self.pos[1] + rem] == -1) or  (vir[self.pos[0] + 1][org[0] + self.pos[1] + rem] == -1) :
		return -1
	elif (vir[self.pos[0]][org[0] + self.pos[1] + rem] == 0) or  (vir[self.pos[0] + 1][org[0] + self.pos[1] + rem] == 0) :
		return 0
	else :
		return 1