# -*- coding: utf-8 -*-


class Stack:
    def __init__(self):
        self.__elements = list()

    def push(self, elem) -> "None":
        self.__elements.append(elem)
    
    def pop(self):
        return self.__elements.pop()
    
    def peek(self):
        return self.__elements[-1]
    
    def isEmpty(self) -> "bool":
        return len(self.__elements) == 0
    
    def size(self) -> "int":
        return len(self.__elements)
    
    def __str__(self):
        return ", ".join(map(str, self.__elements))

class Queue():
    def __init__(self):
        self.__items = list()
    
    def enqueue(self, item) -> "None":
        self.__items.append(item)
    
    def dequeue(self):
        return self.__items.pop(0)
    
    def size(self) -> "int":
        return len(self.__items)

    def isEmpty(self) -> "bool":
        return self.size() == 0

class Deque:
    def __init__(self):
        self.__items = list()
    
    def addFront(self, item) -> "None":
        self.__items.insert(0, item)
    
    def addRear(self, item) -> "None":
        self.__items.append(item)
    
    def size(self) -> "int":
        return len(self.__items)

    def isEmpty(self) -> "bool":
        return self.size() == 0

    def removeFront(self):
        return self.__items.pop(0)
    
    def removeRear(self):
        return self.__items.pop()
