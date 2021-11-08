import math
i = 1
a = 0
out = 0
n = int(input('n = '))
while i <= n:
    a = (i**2)**-1
    out += a
    i += 1
    proc = str(i) + "/" + str(n)
    print(proc, end='\r')
print(math.sqrt(out * 6))
# reference: n = 1x10^8 will calculate 3.1415926 x4498239000 in hour
