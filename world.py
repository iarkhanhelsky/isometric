from utils import  randclr
from random import randint
from rules import rule

def new_object(rows, cols, height): return ((0, 0 , randint(*rows), randint(*cols)), randint(*height), randclr())

def place(object, at):
	((i, j, rows, cols), height, color) = object
	return (at + (rows, cols), height, color)

def populate(n, rows, cols): return [place(obj,(randint(0, rows), randint(0, cols))) for obj in [ new_object((2,8), (2, 8), (20, 50)) for _ in range(n)]]	

 
def cmp_objects(a, b, max): 
	((ai, aj, ar, ac), _, _) = a
	((bi, bj, br, bc), _, _) = b

	return rule(ai + ar, aj , max) - rule(bi + br, bj , max)

def road_populate(w, stop_rows, stop_cols, i0, j0, rows, cols):
    if (rows - i0) > stop_rows and (cols - j0) > stop_cols:

        horisontal = randint(0, 1) == 0
        if horisontal:
            i = randint(i0, rows-1)
            road = (i, j0, 1, cols)
            for j in range(j0, cols):
                w[i][j] = 1
            return [ road_populate(w, stop_rows, stop_cols, i0, j0, i, cols), road_populate(w, stop_rows, stop_cols, i+1, j0, rows, cols), road ]
        else:            
            j = randint(j0, cols-1)
            road = (i0, j, rows-1, 1)
            for i in range(i0, rows):
                w[i][j] = 1            
            return [road_populate(w, stop_rows, stop_cols, i0, j0, rows, j), road_populate(w, stop_rows, stop_cols, i0, j + 1, rows, cols), road]
    else:
        return []            
      
