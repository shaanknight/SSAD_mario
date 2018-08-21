import os

from board import Board
from person import char,Mario

board = Board()
mario = Mario()

while True :
	os.system("tput reset")
	mario.draw(board.box)

	board.draw()
	mario.move(board,board.box)
