import math
x = [1,2,3,4,5,6,7,8,9]

def binary_search(x,a):
    n = len(x)
    inf = 0
    sup = n-1
    while(inf <= sup):
        median = math.floor((inf + sup) / 2)
        if x[median] == a:
            return median
        elif x[median] > x:
            sup = median
        else:
            inf = median
    return -1

print(binary_search(x,5))