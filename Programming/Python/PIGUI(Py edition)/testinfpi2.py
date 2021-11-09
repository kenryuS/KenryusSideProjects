i = 1
n = int(input('n = '))
output = 1
while i <= n:
    output *= (((2*i)/((2*i)-1)))*((2*i)/((2*i)+1))
    print(str(i/n * 100)[:5] + "%", end="\r")
    i += 1

print("\n" + str(output * 2), end="\n")
