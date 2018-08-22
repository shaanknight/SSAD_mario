import random

class Enemy1():

	def __init__(self):
		self.enm = [
			[' ',' ','_','_','_',' '],
			[' ','/',' ','_',' ','\\'],
			['|',' ',' ','_','_','/'],
			[' ','\\','_','_','_','_']
		]

		self.pos_x = random.randint(21,23)
		self.pos_y = random.randint(10,390)

	def draw(self, box, vir, org):
		for i in range(len(self.enm)):
			for j in range(len(self.enm[i])):
				box[self.pos_x + i][org[0] + self.pos_y + j] = self.enm[i][j]
				vir[self.pos_x + i][org[0] + self.pos_y + j] = -1


	def __str__(self):
		return str(self.pos_x) + ',' + str(self.pos_y)

class Enemy2():

	def __init__(self):
		self.enm = [
			['e','e'],
			['"','"']
		]

		self.pos_x = random.randint(21,27)
		self.pos_y = random.randint(10,390)

	def draw(self, box, vir, org):
		for i in range(len(self.enm)):
			for j in range(len(self.enm[i])):
				box[self.pos_x + i][org[0] + self.pos_y + j] = self.enm[i][j]
				vir[self.pos_x + i][org[0] + self.pos_y + j] = -1

	def __str__(self):
		return str(self.pos_x) + ',' + str(self.pos_y)

