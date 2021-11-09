import math
i = 1
a = 0
out = 0
n = int(input('n = '))
while i <= n:
    a = (i**2)**-1
    out += a
    i += 1
    print(str(i/n * 100)[:5] + "%", end="\r")
print("\n" + str(math.sqrt(out * 6)), end="\n")
# reference: n = 1x10^8 will calculate 3.1415926 x4498239000 in hour
