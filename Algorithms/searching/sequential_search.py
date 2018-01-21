x = [1,2,3,4,5,6,7,8,9]

def search(x,a):
    n = len(x)
    for i in range(n):
        if(a == x[i]):
            return i
    return -1

print(search(x,5))