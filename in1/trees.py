# -*- coding: utf-8 -*-

class BinaryTree:
    def __init__(self, rootObj):
        self.__key = rootObj
        self.__leftChild = None
        self.__rightChile = None
    
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
    
    def getRightChild(self) -> "trees.BinaryTree":
        return self.rightChild

    def getLeftChild(self) -> "trees.BinaryTree":
        return self.leftChild

    def setRootVal(self, obj):
        self.__key = obj

    def getRootVal(self):
        return self.__key

    def preorder(self):
        ## preorder traverse
        if self:
            print(self.__key)
            self.getLeftChild().preorder()
            self.getRightChild().preorder()