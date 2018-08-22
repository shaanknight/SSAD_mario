import os
import random

from board import Board
from person import ppl,Mario
from background import Tree,Cloud
from enemy import Enemy1,Enemy2

board = Board()
mario = Mario()
org = [0]
arr_trp = []
arr_cld = []
arr_enm = []

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

	#random enemy generation
	exran = (random.randint(1,10))%2
	if exran == 1 :
		enm = Enemy1()
	else :
		enm = Enemy2()
	if arr_enm == [] :
		arr_enm.append(enm)
		enm.draw(board.box, board.vir, org)

	else :
		for i in arr_enm :
			if abs(enm.pos_y - i.pos_y) > 20:
				if len(arr_enm) <= 10 :
					enm.draw(board.box, board.vir, org)
					arr_enm.append(enm)

	
	board.draw(org)
	mario.move(board,board.box,board.vir,org)



















