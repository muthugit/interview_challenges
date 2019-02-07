import math
inputNumber = 81
for i in range(int(inputNumber/2)):
    for j in range(int(inputNumber/2)):
        if(math.pow(i, j) == inputNumber):
            print("p = "+str(i)+", q = "+str(j))