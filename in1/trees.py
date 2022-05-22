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
    def __init__(self):
        self.__heapList: "list[int]" = [0]
        self.__currentSize: "int" = 0
    
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
        pass

    def __percDown(self, i: "int") -> "None":
        pass

    def __minChild(self, i: "int") -> "int":
        pass

    def __str__(self) -> "str":
        return str(self.__heapList[1:])
    


