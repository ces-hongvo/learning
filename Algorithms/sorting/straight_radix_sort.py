import math
x = [925, 817, 821, 638, 639, 744, 742, 563, 570, 166]
n = len(x)
y = [925, 817, 821, 638, 639, 744, 742, 563, 570, 166]
m = 3 #len of each number in array
def getDigit(x, p, radix):
    return math.floor((x / (radix**p))) % radix

def dCount(x,y,p,radix,n):
    s = [0,0,0,0,0,0,0,0,0,0]
    for i in range(n):
        d = getDigit(x[i], p, radix)
        s[d] += 1
    for i in range(1,10):
        s[i] = s[i-1] + s[i]
    for i in range(n-1, -1, -1):
        d = getDigit(x[i], p, radix)
        y[s[d]-1] = x[i]
        s[d] = s[d] - 1
    print(y)

dCount(x,y,0,10,n)
dCount(y,x,1,10,n)
dCount(x,y,2,10,n)
