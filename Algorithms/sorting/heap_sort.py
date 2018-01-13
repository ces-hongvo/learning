from binary_tree.binary_tree import Node
from binary_tree.binary_tree import generateBinaryTree
from binary_tree.binary_tree import treeToArray
import math

x = [1,2,3,4,5,6,7,8,9]
n = len(x)
depth = round(math.log2(n))
rootNode = generateBinaryTree(depth,x)
rootNode.printTree0()
print("\n")
rootNode.printTree1()
print("\n")
rootNode.printTree2()
print("\n")
s = treeToArray(rootNode, depth)
print(s)
