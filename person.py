import os
import signal
import time
from config import AlarmException, _getChUnix 
from board import Board
from drawnext import paintempty,paintfill
from checkcell import checkh,checkv

class ppl():

	str = []
	pos = []

class enm():

	cfr = []
	pos = []

class Mario(ppl):

	def __init__(self):

		self.str.append(['o','o'])
		self.str.append(['v','v'])
		self.pos.append(26)
		self.pos.append(6)

	def draw(self, box, org):
		for i in range(len(self.str)):
			for j in range(len(self.str[i])):
				box[self.pos[0]+i][org[0]+self.pos[1]+j] = self.str[i][j]

	def move(self, board, box, vir, org):

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
			if checkh(self,vir,org,1) == 1 :
				paintempty(self,box,org)
				org[0] = org[0] + 1
				paintfill(self,box,org)
			elif checkh(self,vir,org,1) == -1:
				quit()

		if c == 'a':
			if checkh(self,vir,org,-1) == 1:
				paintempty(self,box,org)
				org[0] = org[0] - 1
				paintfill(self,box,org)
			elif checkh(self,vir,org,-1) == -1:
				quit()

		if c == 'w':
			while True:
				d = 'p'
				d = action()
				rem = 0
				if d == 'd' :
					rem = 1
				elif d == 'a' :
					rem = -1
				org[0] = org[0] + rem 
				res = checkv(self,vir,org,-1)
				org[0] = org[0] - rem
				if res == -1:
					quit()
				if res == 0:
					break
				os.system("tput reset")
				paintempty(self,box,org)
				self.pos[0] = self.pos[0] - 1
				org[0] = org[0] + rem
				paintfill(self,box,org)
				board.draw(org)
				time.sleep(0.06) 

				if self.pos[0] == 21 :
					break


			while True:
				d = 'p'
				d = action()
				rem = 0
				if d == 'd' :
					rem = 1
				elif d == 'a' :
					rem = -1
				org[0] = org[0] + rem 
				res = checkv(self,vir,org,1)
				org[0] = org[0] - rem
				if res == -1:
					quit()
				if res == 0:
					break
				os.system("tput reset")
				paintempty(self,box,org)
				self.pos[0] = self.pos[0] + 1
				org[0] = org[0] + rem
				paintfill(self,box,org)
				board.draw(org)
				time.sleep(0.06)

				if self.pos[0] == 26 :
					break

