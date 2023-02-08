import math
x = range(2,100)

for i in x:
    a = int(math.pow(i,2))
    if a<=50:
        print(a)