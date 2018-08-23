from random import randint,choice

''' home class '''

class Home():

	def __init__(self):
		self.brk = [
			[' ',' ',' ',' ','\033[1;33m/\033[0m','\033[1;33m\\\033[0m',' ',' ',' ',' '],
			[' ',' ',' ','\033[1;33m/\033[0m',' ',' ','\033[1;33m\\\033[0m',' ',' ',' '],
			[' ',' ','\033[1;33m/\033[0m',' ',' ',' ',' ','\033[1;33m\\\033[0m',' ',' '],
			[' ','\033[1;33m/\033[0m',' ',' ',' ',' ',' ',' ','\033[1;33m\\\033[0m',' '],
			['\033[1;33m/\033[0m','\033[1;33m_\033[0m','\033[1;33m_\033[0m','\033[1;33m_\033[0m','\033[1;33m_\033[0m','\033[1;33m_\033[0m','\033[1;33m_\033[0m','\033[1;33m_\033[0m','\033[1;33m_\033[0m','\033[1;33m\\\033[0m'],
			[' ','\033[1;33m|\033[0m',' ',' ','\033[1;33m_\033[0m','\033[1;33m_\033[0m',' ',' ','\033[1;33m|\033[0m',' '],
			[' ','\033[1;33m|\033[0m',' ','\033[1;33m|\033[0m',' ',' ','\033[1;33m|\033[0m',' ','\033[1;33m|\033[0m',' '],
			['\033[1;33m_\033[0m','\033[1;33m_\033[0m','\033[1;33m_\033[0m','\033[1;33m_\033[0m','\033[1;33m_\033[0m','\033[1;33m_\033[0m','\033[1;33m_\033[0m','\033[1;33m_\033[0m','\033[1;33m_\033[0m','\033[1;33m_\033[0m']
	]
		self.pos_x = 19
		self.pos_y = 375

	def draw(self, box, vir, org):
		for i in range(len(self.brk)):
			for j in range(len(self.brk[i])):
				box[self.pos_x + i][org[0] + self.pos_y + j] = self.brk[i][j]
				vir[self.pos_x + i][org[0] + self.pos_y + j] = 1

	def __str__(self):
		return str(self.pos_x) + ',' + str(self.pos_y)

''' bricks class '''

class Brick():

	def __init__(self):
		self.brk = [
			['\u25A1','\u25A1','\u25A1','\u25A1','\u25A1']
		]

		self.pos_x = randint(22,25)
		self.pos_y = choice([randint(10,120),randint(150,270),randint(300,350)])

	def draw(self, box, vir, org):
		for i in range(len(self.brk)):
			for j in range(len(self.brk[i])):
				box[self.pos_x + i][org[0] + self.pos_y + j] = self.brk[i][j]
				vir[self.pos_x + i][org[0] + self.pos_y + j] = 0

	def __str__(self):
		return str(self.pos_x) + ',' + str(self.pos_y)

''' pillar class '''

class Pillar():

	def __init__(self):
		self.brk = [
			['\u25A1','\u25A1'],
			['\u25A1','\u25A1'],
			['\u25A1','\u25A1']
		]

		self.pos_x = 25
		self.pos_y = choice([randint(10,120),randint(150,270),randint(300,350)])

	def draw(self, box, vir, org):
		for i in range(len(self.brk)):
			for j in range(len(self.brk[i])):
				box[self.pos_x + i][org[0] + self.pos_y + j] = self.brk[i][j]
				vir[self.pos_x + i][org[0] + self.pos_y + j] = 0

	def __str__(self):
		return str(self.pos_x) + ',' + str(self.pos_y)

''' coin class '''

class Coin():

	def __init__(self):
		self.coin = [
			['\033[1;33mO\033[0m'] for i in range(randint(1,4))
		]

		self.pos_x = randint(22,25)
		self.pos_y = randint(10,350)

	def draw(self, box, vir, org):
		for i in range(len(self.coin)):
			for j in range(len(self.coin[i])):
				box[self.pos_x + i][org[0] + self.pos_y + j] = self.coin[i][j]
				vir[self.pos_x + i][org[0] + self.pos_y + j] = 2

	def __str__(self):
		return str(self.pos_x) + ',' + str(self.pos_y)