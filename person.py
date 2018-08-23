import os
import signal
import time
from config import AlarmException, _getChUnix 
from board import Board
from drawnext import paintempty,paintfill
from checkcell import checkh,checkv

''' base class for mario '''

class ppl():

	str = []
	pos = []
	hop = 0
	lives = 0

''' base class for enemy '''	

class enm():

	str = []
	pos = []
	ext = 0
	pos_strt = 0
	pos_end = 0
	pos_old = 0
	dirc = 0

'''mario class'''

class Mario(ppl):

	def __init__(self):

		self.str.append(['o','o'])
		self.str.append(['v','v'])
		self.pos.append(26)
		self.pos.append(6)
		self.hop = 8
		self.lives = 4

	def draw(self, box, vir, org):
		for i in range(len(self.str)):
			for j in range(len(self.str[i])):
				box[self.pos[0]+i][org[0]+self.pos[1]+j] = self.str[i][j]
				vir[self.pos[0]+i][org[0]+self.pos[1]+j] = 3

	def move(self, board, box, vir, org, score, arr_vil, gcnt):

		print('lives = ',self.lives)

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
			gcnt[0] = 0

		if c == 'd':
			res = checkh(self,vir,org,1)
			if res >= 1 :
				paintempty(self,box,org)
				org[0] = org[0] + 1
				paintfill(self,box,vir,org)
			elif checkh(self,vir,org,1) == -1:
				self.lives = self.lives - 1
			if self.lives == 0 :
				gcnt[0] = 0
			if res == 2 :
				score[0] = self.lives*score[0] + self.hop*2 + 1

		if c == 'a':
			res = checkh(self,vir,org,-1) 
			if res >= 1:
				paintempty(self,box,org)
				org[0] = org[0] - 1
				paintfill(self,box,vir,org)
			elif res == -1:
				self.lives = self.lives - 1
			if self.lives == 0 :
				gcnt[0] = 0
			if res == 2:
				score[0] = self.lives*score[0] + self.hop*2 + 1

		if c == 'w':
			while gcnt[0] == 1:

				if self.pos[0] == 20 :
					break
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
					self.lives = self.lives - 1
				if self.lives == 0 :
					gcnt[0] = 0
					break
				if res == 0:
					break
				if res == 2:
					score[0] = self.lives*score[0] + self.hop*2 + 1
				os.system("tput reset")
				paintempty(self,box,org)
				self.pos[0] = self.pos[0] - 1
				org[0] = org[0] + rem
				paintfill(self,box,vir,org)
				for i in arr_vil :
					i.move(vir,gcnt,org,self)
					i.draw(board.box,board.vir,org)
				board.draw(org)
				time.sleep(0.06)

		if c == 's' and self.hop > 0 :
			self.hop = self.hop - 1
			while gcnt[0] == 1:
				if self.pos[0] == 16 :
					break
				org[0] = org[0] + 1 
				res = checkv(self,vir,org,-1)
				org[0] = org[0] - 1
				if res == -1:
					self.lives = self.lives - 1
				if self.lives == 0 :
					gcnt[0] = 0
					break
				if res == 0:
					break
				if res == 2:
					score[0] = self.lives*score[0] + self.hop*2 + 1
				os.system("tput reset")
				paintempty(self,box,org)
				self.pos[0] = self.pos[0] - 1
				org[0] = org[0] + 1
				paintfill(self,box,vir,org)
				for i in arr_vil :
					i.move(vir,gcnt,org,self)
					i.draw(board.box,board.vir,org)
				board.draw(org)
				time.sleep(0.06)

			while True:
				if self.pos[0] == 26 :
					break
				org[0] = org[0] + 1 
				res = checkv(self,vir,org,1)
				org[0] = org[0] - 1
				if res == -1:
					res = 2
				if res == 0:
					break
				if res == 2:
					score[0] = self.lives*score[0] + self.hop*2 + 1
				os.system("tput reset")
				paintempty(self,box,org)
				self.pos[0] = self.pos[0] + 1
				org[0] = org[0] + 1
				paintfill(self,box,vir,org)
				for i in arr_vil :
					i.move(vir,gcnt,org,self)
					i.draw(board.box,board.vir,org)
				board.draw(org)
				time.sleep(0.06)


		while True:
			if self.pos[0] == 26 :
				break
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
				self.lives = self.lives - 1
			if self.lives == 0 :
				gcnt[0] = 0
				break
			if res == 0:
				break
			if res == 2:
				score[0] = self.lives*score[0] + self.hop*2 + 1
			os.system("tput reset")
			paintempty(self,box,org)
			self.pos[0] = self.pos[0] + 1
			org[0] = org[0] + rem
			paintfill(self,box,vir,org)
			for i in arr_vil :
				i.move(vir,gcnt,org,self)
				i.draw(board.box,board.vir,org)
			board.draw(org)
			time.sleep(0.06)

''' enemy class '''

class Enemy1(enm):

	def __init__(self,x,y):
		self.str.append(['*'])
		self.pos.append(26)
		self.pos.append(x)
		self.ext = 1
		self.pos_strt = x
		self.pos_end = y
		self.pos_old = 2
		self.dirc = 1

	def  draw(self, box, vir, org):
		
		box[self.pos[0]][self.pos[1]] = '*'
		box[self.pos[0]][self.pos_old] = ' '
		vir[self.pos[0]][self.pos[1]] = -1
		vir[self.pos[0]][self.pos_old]= 1

	def move(self, vir, gcnt, org, mar):

		self.pos_old = self.pos[1]

		if self.dirc == 1 :
			if self.pos[1] < self.pos_end :
				self.pos[1] = self.pos[1] + 1
			else :
				self.pos[1] = self.pos[1] - 1
				self.dirc = -1

		else :
			if self.pos[1] > self.pos_strt :
				self.pos[1] = self.pos[1] - 1
			else :
				self.pos[1] = self.pos[1] + 1
				self.dirc = 1

		for i in range(len(mar.str)):
			for j in range(len(mar.str[i])):
				if mar.pos[0]+i == self.pos[0] and org[0]+mar.pos[1]+j == self.pos[1] :
					gcnt[0] = 0
					break

























