def summ(n):
    return (1 + n) * n // 2


def rule(i, j, max_rows):
    return summ(max_rows - i + j - 1) + j


def generate(n, m, max_rows):
    return [[rule(i, j, max_rows) for i in range(n)] for j in range(m)]