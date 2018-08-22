import os
import random

from board import Board
from person import ppl,Mario
from background import Tree,Cloud
from obstacles import Cactus,Brick

board = Board()
mario = Mario()
org = [0]
arr_trp = []
arr_cld = []
arr_cct = []
arr_brk = []

while True :
	os.system("tput reset")
	mario.draw(board.box, org)

	trp = Tree()

	if arr_trp != []:
		for i in arr_trp:
			if abs(trp.pos_y - i.pos_y) > 10:
				if len(arr_trp) <= 20:
					trp.draw(board.box, org)
					arr_trp.append(trp)

	else:
		arr_trp.append(trp)
		trp.draw(board.box,org)

	cld = Cloud()

	if arr_cld != []:
		for i in arr_cld:
			if abs(cld.pos_y - i.pos_y) > 10:
				if len(arr_cld) <= 20:
					cld.draw(board.box, org)
					arr_cld.append(cld)

	else:
		arr_cld.append(cld)
		cld.draw(board.box, org)

	cct = Cactus()

	if arr_cct != []:
		for i in arr_cct:
			if abs(cct.pos_y - i.pos_y) > 10:
				if len(arr_cct) <= 20:
					cct.draw(board.box, board.vir, org)
					arr_cct.append(cct)

	else:
		arr_cct.append(cct)
		cct.draw(board.box,board.vir,org)
	
	brk = Brick()

	if arr_brk != []:
		for i in arr_brk :
			if abs(brk.pos_y - i.pos_y) > 10:
				if len(arr_brk) <= 20:
					brk.draw(board.box, board.vir, org)
					arr_brk.append(brk)

	else:
		arr_brk.append(brk)
		brk.draw(board.box,board.vir,org)

	
	board.draw(org)
	mario.move(board,board.box,board.vir,org)



















