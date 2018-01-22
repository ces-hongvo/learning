from binary_tree.binary_tree import Node
from binary_tree.binary_tree import treeToArray
x = [4,2,6,1,3,5,7,9]
n = len(x)
rootNode = Node(None)
for i in range(n):
    rootNode.makeBST(x[i])

rootNode.deleteInBST(4)
rootNode.printTree0()
print("")
rootNode.printTree1()
print("")
rootNode.printTree2()
