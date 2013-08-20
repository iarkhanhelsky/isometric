from utils import  randclr
from random import randint
from rules import rule

def new_object(rows, cols, height): return ((0, 0 , randint(*rows), randint(*cols)), randint(*height), randclr())

def place(object, at):
	((i, j, rows, cols), height, color) = object
	return (at + (rows, cols), height, color)

 
def cmp_objects(a, b): 
	((ai, aj, ar, ac), _, _) = a
	((bi, bj, br, bc), _, _) = b

	return rule(ai + ar, aj + ac, 300) - rule(bi + br, bj + bc, 300)