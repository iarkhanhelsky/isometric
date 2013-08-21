from random import randint  

CELL_WITH = 16
CELL_HEIGHT = 8

COLORS = 255 * 255 * 255

def ij_to_xy(i, j): return (8 * (i + j), 4 * (j - i) )
 
def randclr(): return randint(0, 255 * 255 * 255)