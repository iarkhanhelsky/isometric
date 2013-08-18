from utils import rand, randclr
from random import randint

def new_object(rows, cols, height): return ((0, 0 , randint(*rows), randint(*cols)), randint(*height), randclr())

def place(object, at):
	((i, j, rows, cols), height, color) = object
	return (at + (rows, cols), height, color)