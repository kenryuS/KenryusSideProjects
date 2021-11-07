import random
from tqdm import tqdm , trange
n = input('n = ')
n1 = input('number of trials: ')

def montecalro(n,n1):
    """
    n = number of point to be placed on the plane
    n1 = number of the trials
    """
    finaloutput = float(0)
    DATA = []
    outputlist = []
    i1 = 0
    i2 = 0
    while i1 < n1:
        i = x = y = z = a = 0
        output = ""
        pbar = tqdm(total=n)
        while i < n:
            x = random.random()
            y = random.random()
            z = (x**2) + (y**2)
            if z >= float(1):
                pass
            elif z < float(1):
                a += 1
            i += 1
            pbar.update(1)
        pbar.close()
        output = (a/n) * 4
        print(output)
        DATA.append(output)
        i1 += 1
    while i2 < len(DATA):
        finaloutput += DATA[i2]
        i2 += 1
    finaloutput = finaloutput/len(DATA)
    return finaloutput

print(montecalro(int(n),int(n1)))
