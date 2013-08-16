
def summ(n): return (1 + n) * n // 2

def rule(i, j, max): return summ(max - i + j - 1) + j

def generate(n, m, max): return [ [ rule(i, j, max) for i in range(n) ] for j in range(m) ]