# -*- coding: utf-8 -*-

import linear



def binarySearch():
    pass

def bubbleSort(c: "list") -> "None":
    for i in range(len(c)):
        for j in range(len(c) - i - 1):
            if c[j] > c[j + 1]:
                temp = c[j]
                c[j] = c[j + 1]
                c[j + 1] = temp

def mergeSort():
    pass

def quickSort(c):
    quickSortHelper(c, 0, len(c) - 1)

def quickSortHelper(c, first, last):
    if first < last:
        ## find splitting point
        split_point = partition(c, first, last)
        ## recursively sort the first half
        quickSortHelper(c, first, split_point - 1)
        ## recursively sort the latter half
        quickSortHelper(c, split_point + 1, last)

def partition(c, first, last):
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
    print("Bianry Search")
    print("=" * 100)
    print("Bubble Sort [25, 65, 897, 23, 765,1234, 897, 23, 67]")
    tc1 = [25, 65, 897, 23, 765,1234, 897, 23, 67]
    bubbleSort(tc1)
    print(tc1)
    print("=" * 100)
    print("Merge Sort")
    print("=" * 100)
    print("Quick Sort")
    print("=" * 100)

if __name__ == "__main__":
    main()
