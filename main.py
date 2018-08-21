import os

from board import Board
from person import char,Mario

board = Board()
mario = Mario()
org = [0]

while True :
	os.system("tput reset")
	mario.draw(board.box,org)

	board.draw(org)
	mario.move(board,board.box,org)
