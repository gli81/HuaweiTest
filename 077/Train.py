# -*- coding: utf-8 -*-

class Train:
    def train(self, a, cmp):
        pass
    
    def check(self, a, cmp):
        stk = []
        j = i = 0
        for i in range(len(a)):
            stk.append(a[i])
            while j < len(a) and len(stk) != 0 and cmp[j] == stk[len(stk) - 1]:
                stk.pop()
                j += 1