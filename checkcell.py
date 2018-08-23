''' utility functions to check the status of exact next position reached by mario horizontally as well as vertically ''' 

def checkh(self, vir, org, rem):
	fl = 1
	for i in range(2):
		for j in range(2):
			if vir[self.pos[0] + i][org[0] + self.pos[1] + j + rem] == -1 :
				return -1
			fl = fl*vir[self.pos[0] + i][org[0] + self.pos[1] + j + rem]
	return fl

def checkv(self, vir, org, rem):
	fl = 1
	for i in range(2):
		for j in range(2):
			if vir[self.pos[0] + rem + i][org[0] + self.pos[1] + j] == -1 :
				return -1
			fl = fl*vir[self.pos[0] + rem + i][org[0] + self.pos[1] + j]
	return fl