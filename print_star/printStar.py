maxRows = 10
maxCols = 100
for i in range(maxRows):
    star = "*"
    for j in range(maxCols-2):
        if(i==0 or i==maxRows-1):
            star = star + "*"
        else:
            star = star + " "
    print(star+"*")