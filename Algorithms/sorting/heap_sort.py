from binary_tree.binary_tree import Node
from binary_tree.binary_tree import generateBinaryTree
from binary_tree.binary_tree import treeToArray
from binary_tree.binary_tree import generateHeap
import math

x = [1,2,3,4,5,6,7,8,9]
n = len(x)
depth = round(math.log2(n))
rootNode = generateBinaryTree(depth,x)
s = treeToArray(rootNode, depth)
print(s)
rootHeap = generateHeap(depth , x)
sHeap = treeToArray(rootHeap, depth)
print(sHeap)

n0 = [4,8,6,7,3,2,5,1]
tmpRoot = generateBinaryTree(depth, n0)
print(treeToArray(tmpRoot, depth))
tmpRoot.adjustHeap()
print(treeToArray(tmpRoot, depth))