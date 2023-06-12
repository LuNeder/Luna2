import math
#campo esperado
i = input().split()
print(i)
for z in i:
    z = float(z)/100

    b = str(((((4*math.pi*(10**(-7))*1.04)/2)*((0.15**2)/(((z**2)+(0.15**2)))**(3/2))))*130*10).replace('.', ',')
    print(b)

