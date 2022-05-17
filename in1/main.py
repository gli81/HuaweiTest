# -*- coding: utf-8 -*-

import linear



def binarySearch():
    pass


def main():
    stk1 = linear.Stack()
    print(stk1.isEmpty())
    stk1.push(2)
    stk1.push(5)
    print(stk1)
    print(stk1.pop())
    print(stk1)
    stk1.push(5)
    stk1.push(7)
    print(stk1.peek())
    print(stk1)
    print(stk1.isEmpty())
    print(stk1.size())
    print("=" * 100)

if __name__ == "__main__":
    main()