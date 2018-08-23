''' class for board '''

class Board:

	box = [[' ' for j in range(400)] for i in range(32)]
	vir = [[1 for j in range(400)] for i in range(32)]

	def __init__(self):
		
		for i in range(4):
			for j in range(0,400,4):
				self.box[i][j] = '\033[1;49m|\033[0m'
				self.box[i][j+1] = '\033[1;49m_\033[0m'
				self.box[i][j+2] = '\033[1;49m_\033[0m'
				self.box[i][j+3] = '\033[1;49m_\033[0m'
				self.vir[i][j] = 0
				self.vir[i][j+1] = 0
				self.vir[i][j+2] = 0
				self.vir[i][j+3] = 0

				if i == 0 or i == 1 or i==2:
					self.box[31-i][j] = '\033[1;49m|\033[0m'

				else :
					self.box[31-i][j] = '\033[1;49m_\033[0m'

				self.vir[31-i][j] = 0

				self.box[31-i][j+1] = '\033[1;49m_\033[0m'
				self.box[31-i][j+2] = '\033[1;49m_\033[0m'
				self.box[31-i][j+3] = '\033[1;49m_\033[0m'
				self.vir[31-i][j+1] = 0
				self.vir[31-i][j+2] = 0
				self.vir[31-i][j+3] = 0

	def draw(self, org):

		for i in self.box:
			temp = ''
			for j in i[org[0]:org[0]+80]:
				temp += j
			print(temp)
