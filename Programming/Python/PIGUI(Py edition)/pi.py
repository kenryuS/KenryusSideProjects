import math
import random
def montecalro(n):
    a = 0
    i = 0
    while i <= n:
        x = random.random()
        y = random.random()
        z = (x**2) + (y**2)
        if z >= 1:
            a += 1
        else:
            a = a
    print(a)

montecalro(int(input('n = ')))