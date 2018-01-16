from binary_tree.binary_tree import Node
from binary_tree.binary_tree import generateBinaryTree
from binary_tree.binary_tree import treeToArray
from binary_tree.binary_tree import generateHeap
import math

x = [5, 1, 4, 2, 9, 3, 6, 8, 7]
n = len(x)
depth = round(math.log2(n) - 0.5)

rootHeap = generateHeap(depth , x)
sHeap = treeToArray(rootHeap, depth)
result = []
while(len(sHeap) > 0):
    last = len(sHeap) - 1
    tmp = sHeap[0]
    sHeap[0] = sHeap[last]
    sHeap[last] = tmp
    lastElement = sHeap.pop()
    result.insert(0,lastElement)
    if(last != 0):
        rawDepth = math.log2(last)
    else:
        rawDepth = 0
    if(rawDepth == 0):
        depth = 0
    else:
        depth = math.floor(rawDepth)
    if(len(sHeap) < 1):
        break
    rootHeap = generateHeap(depth, sHeap)
    sHeap = treeToArray(rootHeap, depth)

print(result)