# -*- coding: utf-8 -*-

class BinaryTree:
    def __init__(self, rootObj, leftChild = None, rightChild = None):
        self.__key = rootObj
        self.__leftChild = leftChild
        self.__rightChild = rightChild

    def insertLeft(self, newNode) -> "None":
        if self.__leftChild == None:
            self.__leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.__leftChild = self.__leftChild
            self.__leftChild = t

    def insertRight(self, newNode) -> "None":
        if self.__rightChild == None:
            self.__rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.__rightChild = self.__rightChild
            self.__rightChild = t

    def getRightChild(self) -> "BinaryTree":
        return self.__rightChild

    def getLeftChild(self) -> "BinaryTree":
        return self.__leftChild

    def setRootVal(self, obj):
        self.__key = obj

    def getRootVal(self):
        return self.__key

    def preorder(self):
        ## preorder traverse
        print(self.getRootVal())
        if self.getLeftChild():
            self.getLeftChild().preorder()
        if self.getRightChild():
            self.getRightChild().preorder()

    def inorder(self):
        ## inorder traverse
        if self.getLeftChild():
            self.getLeftChild().inorder()
        print(self.getRootVal())
        if self.getRightChild():
            self.getRightChild().inorder()

    def postorder(self):
        ## postorder traverse
        if self.getLeftChild():
            self.getLeftChild().postorder()
        if self.getRightChild():
            self.getRightChild().postorder()
        print(self.getRootVal())

class BinaryHeap():
    '''
    the heap is represented by a list\n
    each node has a index x, its left child's index would be 2x, right child's index would be 2x+1\n
    a node with index y has a parent with index y//2 \n
    (due to complete binary tree's property)\n
    compelete binary tree: leaves only at bottom level, or last but second level\n
    every internal node has two children, only one exception
    '''
    def __init__(self, heapList = [0], currentSize = 0):
        self.__heapList: "list[int]" = heapList
        self.__currentSize: "int" = currentSize
    
    def insert(self, key: "int") -> "None":
        self.__heapList.append(key)
        self.__currentSize += 1
        self.__percUp(self.__currentSize)

    def __percUp(self, i: "int") -> "None":
        while i > 1:
            if self.__heapList[i] < self.__heapList[i // 2]:
                self.__heapList[i], self.__heapList[i // 2] = self.__heapList[i // 2], self.__heapList[i]
            i = i // 2

    def delMin(self) -> "None":
        ans = self.__heapList[1]
        self.__heapList[1] = self.__heapList[self.__currentSize]
        self.__heapList.pop()
        self.__currentSize -= 1
        self.__percDown(1)  ## move the last one to the top, then sink it to the proper position
        return ans

    def __percDown(self, i: "int") -> "None":
        while i * 2 <= self.__currentSize: ## current node has at least one child
            min_child_index = self.__minChild(i)
            if self.__heapList[i] > self.__heapList[min_child_index]:
                self.__heapList[i], self.__heapList[min_child_index] = self.__heapList[min_child_index], self.__heapList[i]
            i = min_child_index

    def __minChild(self, i: "int") -> "int":
        ## only one child
        if i * 2 + 1 > self.__currentSize:
            return i * 2
        else:
            return i * 2 if self.__heapList[i * 2] <= self.__heapList[i * 2 + 1] else i * 2 + 1

    @staticmethod
    def buildHeap(alist: "list[int]") -> "BinaryHeap":
        ## start from the last node's parent
        i = len(alist) // 2
        sz = len(alist)
        hlist = [0] + alist[:]
        bh = BinaryHeap(hlist, sz)
        while i > 0:
            bh.__percDown(i)
            i -= 1
        return bh

    def __str__(self) -> "str":
        return str(self.__heapList[1:])
    
class BinarySearchTree:
    def __init__(self):
        pass

class TreeNode:
    def __init__(self, key, val, left = None, right = None, parent = None):
        self.__key = key
        self.__val = val
        self.__left = left
        self.__right = right
        self.__parent = parent
    
    def hasLeftChild(self) -> "bool":
        return self.__left

    def hasRightChild(self) -> "bool":
        return self.__right

    def getLeftChild(self) -> "TreeNode":
        return self.__left
    
    def getRightChild(self) -> "TreeNode":
        return self.__right
    
    def getParent(self) -> "TreeNode":
        return self.__parent
    
    def setLeftChild(self, lc: "TreeNode") -> "None":
        self.__left = lc
    
    def setRightChild(self, rc: "TreeNode") -> "None":
        self.__right = rc
    
    def setParent(self, parent: "TreeNode") -> "None":
        self.__parent = parent
    
    def isLeftChild(self) -> "bool":
        return self.__parent and self.__parent.getLeftChild() == self

    def isRightChild(self) -> "bool":
        return self.__parent and self.__parent.getRightChild() == self
    
    def isRoot(self) -> "bool":
        return not self.__parent
    
    def hasAnyChildren(self) -> "bool":
        return self.__right or self.__left
    
    def hasBothChildren(self) -> "bool":
        return self.__right and self.__left
    
    def replaceNodeData(self, key, value, lc: "TreeNode", rc: "TreeNode"):
        self.__key = key
        self.__val = value
        self.__left = lc
        self.__right = rc
        if self.hasLeftChild():
            self.__left.setParent(self)
        if self.hasRightChild():
            self.__right.setParent(self)
        