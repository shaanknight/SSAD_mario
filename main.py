''' The whole game is co-ordinated here '''

import os 
import random
import time
from board import Board
from person import ppl,Mario,enm,Enemy1
from background import Tree,Cloud,show1,show2
from neighbours import Brick,Coin,Pillar,Home
from opponents import Cactus,Opp1,Opp2,Opp3

print('\t\t\t\t Welcome to the World Of Little Mario')
print('\t\t\t\t Start playing on pressing any key and enter')
s = input()

board = Board()
mario = Mario()
org = [0]
arr_trp = []
arr_cld = []
arr_cct = []
arr_brk = []
arr_coin = []
arr_plr = []
arr_enm = []
arr_vil = []
vil1 = Enemy1(125,145)
arr_vil.append(vil1)
score = [0]
gcnt = [1]
ch = 0
sh1 = 0
sh2 = 0
strt_time = time.time()
os.system('aplay -qN ./theme.wav &')

while True :
	os.system("tput reset")
	''' movement and drawing of mario and enemy '''
	if time.time() - strt_time > 89 :
		os.system("aplay -qN ./theme.wav &")

	mario.draw(board.box,board.vir,org)
	for i in arr_vil :
		i.move(board.vir,gcnt,org,mario)
		#print(i.pos_strt,':',i.pos[1])
		i.draw(board.box,board.vir,org)

	''' display of levels '''

	sho1 = show1()
	sh1 = sh1 + 1

	if sh1 == 1:
		sho1.draw(board.box,org)

	sho2 = show2()
	sh2 = sh2 + 1

	if sh2 == 1:
		sho2.draw(board.box,org)

	''' display of home '''

	hom = Home()
	ch = ch + 1

	if ch == 1 :
		hom.draw(board.box,board.vir,org)

	''' display of trees in background '''

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

	''' display of clouds in  background '''

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

	''' display of cactus - a potential opponent '''

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
	
	''' display of bricks in between - stops you and also serves as a platform '''

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

	''' display of pillars - stops you and also serves as a platform '''

	plr = Pillar()

	if arr_plr != []:
		for i in arr_plr :
			if abs(plr.pos_y - i.pos_y) > 10:
				if len(arr_plr) <= 20:
					plr.draw(board.box, board.vir, org)
					arr_plr.append(plr)

	else:
		arr_plr.append(plr)
		plr.draw(board.box,board.vir,org)

	''' display of coins - which gives you score '''

	con = Coin()

	if arr_coin != []:
		for i in arr_coin :
			if abs(con.pos_y - i.pos_y) > 10:
				if len(arr_coin) <= 100:
					con.draw(board.box, board.vir, org)
					arr_coin.append(con)

	else:
		arr_coin.append(con)
		con.draw(board.box,board.vir,org)

	''' display of opponents - a monkey king and few other aliens '''

	x = random.randint(1,3)

	if x == 1 :
		enm = Opp1()
	elif x == 2 :
		enm = Opp2()
	else :
		enm = Opp3()

	if arr_enm != []:
		for i in arr_enm :
			if abs(enm.pos_y - i.pos_y) > 10:
				if len(arr_enm) <= 20:
					enm.draw(board.box, board.vir, org)
					arr_enm.append(enm)

	else:
		arr_enm.append(enm)
		enm.draw(board.box,board.vir,org)


	board.draw(org)
	mario.move(board,board.box,board.vir,org,score,arr_vil,gcnt)

	if gcnt[0] == 0:
		print('\t\t\t You have not been able to successfully complete the game.')
		print('\t\t\t\t\t score=',score[0])
		os.system('pkill -kill aplay')
		quit()

	if org[0] >=369 :
		print('\t\t\t Successful !!')
		print('\t\t\t score = ',score[0])
		os.system('pkill -kill aplay')
		quit()






















