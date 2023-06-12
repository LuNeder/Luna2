import math
#campo real
i = input().split()
print(i)
for z in i:
    z = float(z)/100

    b = str((z*0.00395)).replace('.', ',')
    print(b)

