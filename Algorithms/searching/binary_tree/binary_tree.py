from __future__ import print_function

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
    
    def adjustHeap(self):
        leftKey = 0
        rightKey = 0
        maxChild = None
        if(self.left != None):
            leftKey = self.left.key
        if(self.right != None):
            rightKey = self.right.key
        if(leftKey > rightKey):
            maxChild = self.left
        elif(leftKey < rightKey):
            maxChild = self.right
        if(maxChild.key > self.key):
            tmp = self.key
            self.key = maxChild.key
            maxChild.key = tmp
            maxChild.adjustHeap()

    def makeBST(self, x):
        if(self.key == None):
            self.key = x
            return self
        q = self
        while(q != None):
            if(q.key == x):
                return self
            elif (q.key > x):
                if(q.left != None):
                    q = q.left
                else:
                    q.insertLeft(Node(x))
                    return self
            elif (q.key < x):
                if(q.right != None):
                    q = q.right
                else:
                    q.insertRight(Node(x))
                    return self
        return self

    def deleteInBST(self, x):
        p = self
        q = None #hold the parent during search
        pNode = None #hold the processing node
        cNode = None #hold the child node
        while p != None:
            if p.key == x:
                break
            q = p
            if (x < p.key):
                p = p.left
            if (x > p.key):
                p = p.right
        if p == None:
            return
        if (p.left != None and p.right != None):
            pNode = p
            q = p
            p = p.left
            while(p.right != None):
                q = p
                p = p.right
            pNode.key = p.key
        else:
            q = p.parent
        if(p.left != None):
            cNode = p.left
        else:
            cNode = p.right
        if q.left == p:
            q.left = cNode
        else:
            q.right = cNode
        return

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
            nodeList[j].insertLeft(Node(x[tmp]))
            tmp += 1
            if(tmp > n-1):
                break
            nodeList[j].insertRight(Node(x[tmp]))
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

def generateHeap(depth, x):
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
            nodeList[j].insertLeft(Node(x[tmp]))
            heapingNode(nodeList[j].left)
            tmp += 1
            if(tmp > n-1):
                break
            nodeList[j].insertRight(Node(x[tmp]))
            heapingNode(nodeList[j].right)
            tmp += 1
            newNodeList.append( nodeList[j].left)
            newNodeList.append( nodeList[j].right)
        nodeList = newNodeList
    return rootNode

def heapingNode(node):
    while(node.parent != None):
        if(node.key > node.parent.key):
            tmp = node.key
            node.key = node.parent.key
            node.parent.key = tmp
            node = node.parent
        else:
            break
