import os
import signal
import time
from config import AlarmException, _getChUnix 
from board import Board
from drawnext import paintempty,paintfill

class char():

	str = []
	pos = []

class Mario(char):

	def __init__(self):

		self.str.append(['o','o'])
		self.str.append(['v','v'])
		self.pos.append(26)
		self.pos.append(6)

	def draw(self, box):
		for i in range(len(self.str)):
			for j in range(len(self.str[i])):
				box[self.pos[0]+i][self.pos[1]+j] = self.str[i][j]

	def move(self, board, box):

		def alarmhandler(signum, frame):
			raise AlarmException

		def action(timeout=0.1):

			signal.signal(signal.SIGALRM, alarmhandler)
			signal.setitimer(signal.ITIMER_REAL, timeout)
			try:
			    text = _getChUnix()()
			    signal.alarm(0)
			    return text
			except AlarmException:
			    pass
			signal.signal(signal.SIGALRM, signal.SIG_IGN)
			return ''

		c = action()

		if c == 'q':
			quit()

		if c == 'd':
			paintempty(self,box)
			self.pos[1] = self.pos[1] + 1
			paintfill(self,box)

		if c == 'a':
			paintempty(self,box)
			self.pos[1] = self.pos[1] - 1
			paintfill(self,box)

		if c == 'w':
			for i in range(3):
				os.system("tput reset")
				paintempty(self,box)
				self.pos[0] = self.pos[0] - 2
				d = 'p'
				d = action()
				if d == 'd':
					self.pos[1] = self.pos[1] + 1
				elif d == 'a' :
					self.pos[1] = self.pos[1] - 1

				paintfill(self,box)
				board.draw()
				time.sleep(0.06) 

			for i in range(3):
				os.system("tput reset")
				paintempty(self,box)
				self.pos[0] = self.pos[0] + 2
				d = 'p'
				d = action()
				if d == 'd':
					self.pos[1] = self.pos[1] + 1
				elif d == 'a' :
					self.pos[1] = self.pos[1] - 1

				paintfill(self,box)
				board.draw()
				time.sleep(0.06)

















