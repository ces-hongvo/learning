class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def insertLeft(self, t):
        self.left = t
        t.parent = self

    def insertRight(self, t):
        self.right = t
        t.parent = self

    def printTree0(self):
        if(self.left != None):
            self.left.printTree0()
        if(self.right != None):
            self.right.printTree0()
        print(self.key, end=" ")
    
    def printTree1(self):
        if(self.left != None):
            self.left.printTree1()
        print(self.key, end=" ")
        if(self.right != None):
            self.right.printTree1()
    
    def printTree2(self):
        print(self.key, end=" ")
        if(self.left != None):
            self.left.printTree2()
        if(self.right != None):
            self.right.printTree2()

def generateBinaryTree(depth, x):
    n = len(x)
    rootNode = Node(x[0])
    nodeList = [rootNode]
    tmp = 1
    for i in range(0, depth):
        newNodeList = []
        upBound = 2*i
        if(upBound == 0):
            upBound = 1
        for j in range(upBound):
            if(tmp > n-1):
                break
            nodeList[j].left = Node(x[tmp])
            tmp += 1
            if(tmp > n-1):
                break
            nodeList[j].right = Node(x[tmp])
            tmp += 1
            newNodeList.append( nodeList[j].left)
            newNodeList.append( nodeList[j].right)
        nodeList = newNodeList
    return rootNode

def treeToArray(rootNode = Node(0), depth = 0):
    nodeList = [rootNode]
    arrayResult = [rootNode.key]
    for i in range(0, depth):
        newNodeList = []
        upBound = 2*i
        if(upBound == 0):
            upBound = 1
        for j in range(upBound):
            if(nodeList[j].left != None):
                arrayResult.append(nodeList[j].left.key)
            if(nodeList[j].right != None):
                arrayResult.append(nodeList[j].right.key)
            newNodeList.append( nodeList[j].left)
            newNodeList.append( nodeList[j].right)
        nodeList = newNodeList
    return arrayResult
