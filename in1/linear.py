# -*- coding: utf-8 -*-


class Stack:
    def __init__(self):
        self.__elements = list()

    def push(self, elem):
        self.__elements.append(elem)