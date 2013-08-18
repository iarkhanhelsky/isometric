from utils import rand, randclr
from random import randint

def building(rows, cols, height): return ((0, 0 , randint(*rows), randint(*cols)), randint(*height), randclr())
