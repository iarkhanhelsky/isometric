from random import randint  

CELL_WITH = 32
CELL_HEIGHT = 16

COLORS = 255 * 255 * 255

def ij_to_xy(i, j): return (32 * (i + j) // 2, 16 * (j - i) // 2)

def randclr(): return rand(255 * 255 * 255)