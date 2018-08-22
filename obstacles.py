import random

class Cactus():

	def __init__(self):
		self.enm = [
			['c'],
			['"']
		]

		self.pos_x = 26
		self.pos_y = random.randint(10,390)

	def draw(self, box, vir, org):
		for i in range(len(self.enm)):
			for j in range(len(self.enm[i])):
				box[self.pos_x + i][org[0] + self.pos_y + j] = self.enm[i][j]
				vir[self.pos_x + i][org[0] + self.pos_y + j] = -1

	def __str__(self):
		return str(self.pos_x) + ',' + str(self.pos_y)

class Brick():

	def __init__(self):
		self.brk = [
			['\u25A1','\u25A1','\u25A1','\u25A1','\u25A1']
		]

		self.pos_x = random.randint(21,25)
		self.pos_y = random.randint(10,390)

	def draw(self, box, vir, org):
		for i in range(len(self.brk)):
			for j in range(len(self.brk[i])):
				box[self.pos_x + i][org[0] + self.pos_y + j] = self.brk[i][j]
				vir[self.pos_x + i][org[0] + self.pos_y + j] = 0

	def __str__(self):
		return str(self.pos_x) + ',' + str(self.pos_y)
