from random import randint,choice

''' cactus class '''

class Cactus():

	def __init__(self):
		self.enm = [
			['\033[1;32m"\033[0m'],
			['\033[1;32m"\033[0m']
		]

		self.pos_x = 26
		self.pos_y = choice([randint(10,120),randint(150,270),randint(300,350)])

	def draw(self, box, vir, org):
		for i in range(len(self.enm)):
			for j in range(len(self.enm[i])):
				box[self.pos_x + i][org[0] + self.pos_y + j] = self.enm[i][j]
				vir[self.pos_x + i][org[0] + self.pos_y + j] = -1

	def __str__(self):
		return str(self.pos_x) + ',' + str(self.pos_y)

''' alien1 class '''

class Opp1():

	def __init__(self):
		self.enm = [
			['e','_','e'],
			[' ','e',' '],
			['=','=','=']
		]

		self.pos_x = 23
		self.pos_y = choice([randint(10,120),randint(150,270),randint(300,350)])

	def draw(self, box, vir, org):
		for i in range(len(self.enm)):
			for j in range(len(self.enm[i])):
				box[self.pos_x + i][org[0] + self.pos_y + j] = self.enm[i][j]
				vir[self.pos_x + i][org[0] + self.pos_y + j] = -1


	def __str__(self):
		return str(self.pos_x) + ',' + str(self.pos_y)

''' frown man class ''' 

class Opp2():

	def __init__(self):
		self.enm = [
			['\033[1;35m^\033[0m','\033[1;35m_\033[0m','\033[1;35m^\033[0m'],
			['\033[1;35m\\\033[0m','\033[1;35m-\033[0m','\033[1;35m/\033[0m']
		]

		self.pos_x = 23
		self.pos_y = choice([randint(10,120),randint(150,270),randint(300,350)])

	def draw(self, box, vir, org):
		for i in range(len(self.enm)):
			for j in range(len(self.enm[i])):
				box[self.pos_x + i][org[0] + self.pos_y + j] = self.enm[i][j]
				vir[self.pos_x + i][org[0] + self.pos_y + j] = -1


	def __str__(self):
		return str(self.pos_x) + ',' + str(self.pos_y)

''' monkey king class '''

class Opp3():

	def __init__(self):
		self.enm = [
			['\033[1;35m{','\033[1;35m\\','\033[1;35m(','\033[1;35m)','\033[1;35m(','\033[1;35m)','\033[1;35m/','\033[1;35m}'],
			[' ',' ',' ','\033[1;35m/','\033[1;35m;',' ',' ',' '],
			[' ',' ','\033[1;35m\\','\033[1;35m_','\033[1;35m_','\033[1;35m/',' ']
		]

		self.pos_x = 24
		self.pos_y = choice([randint(10,120),randint(150,270),randint(300,350)])

	def draw(self, box, vir, org):
		for i in range(len(self.enm)):
			for j in range(len(self.enm[i])):
				box[self.pos_x + i][org[0] + self.pos_y + j] = self.enm[i][j]
				vir[self.pos_x + i][org[0] + self.pos_y + j] = -1


	def __str__(self):
		return str(self.pos_x) + ',' + str(self.pos_y)

'''{\()()/}
   ;;
  \__/'''