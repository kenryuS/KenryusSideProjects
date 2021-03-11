import math
import time
i = 1
r = (2*math.pi / 360)
while i == 1:
    print("Opperate sin(a+b)")
    a = r*float(input("input for a in degree"))
    b = r*float(input("input for b in degree"))
    print("Opperatting...")
    time.sleep(3)
    s = (math.sin(a)*math.cos(b))+(math.cos(a)*math.sin(b))
    print(s)
    c = input("Continue?[y/n]:")
    if c == "n":
        break
