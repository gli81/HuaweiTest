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

    def getRightChild(self) -> "trees.BinaryTree":
        return self.__rightChild

    def getLeftChild(self) -> "trees.BinaryTree":
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
