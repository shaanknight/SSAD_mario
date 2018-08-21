class Board:

	box = [[' ' for j in range(80)] for i in range(32)]

	def __init__(self):
		
		for i in range(4):
			for j in range(0,80,4):
				self.box[i][j] = '|'
				self.box[i][j+1] = '_'
				self.box[i][j+2] = '_'
				self.box[i][j+3] = '_'

				if i == 0 or i == 1 or i==2:
					self.box[31-i][j] = '|'

				self.box[31-i][j+1] = '_'
				self.box[31-i][j+2] = '_'
				self.box[31-i][j+3] = '_'

	def draw(self):

		for i in self.box:
			temp = ''
			for j in i:
				temp += j
			print(temp)