print("Gregory-Leibniz series")
i = 1
n = int(input('n = '))
output = 0
while i <= n:
    output += ((-1)**(i-1)) * 4/((2*i)-1)
    print(str((i/n)*100)[:5] + "%", end="\r")
    i += 1

print("\n" + str(output))
