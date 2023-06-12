import math
#campo esperado - TA ERRADO
i = input().split()
print(i)
for z in i:
    z = float(z)/100

    b = str((((4*math.pi*(10**(-7))*1.01*(0.15**2))/2)*((1/((z-(0.15/2)**2+0.15**2)**(3/2))+1/((z+(0.15/2)**2+0.15**2)**(3/2)))))/(10**(-3))).replace('.', ',')
    print(b)

