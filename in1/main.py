# -*- coding: utf-8 -*-

import linear
import trees
import graph

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

def partition(c, first, last) -> "int":
    pivot = first
    left = first
    right = last
    while left < right:
        while left < right and c[right] >= c[pivot]:
            ## if c[right] keeps being greater than c[pivot], right pointer moves left until go beyond the other pointer
            right -= 1
        while left < right and c[left] <= c[pivot]:
            ## if c[left] keeps being smaller than c[pivot], left pointer moves right until go beyond the other pointer
            left += 1
        if left < right: ## find one smaller than pivot, and one larger than pivot, smaller one left side of larger one
            ## swap
            temp = c[left]
            c[left] = c[right]
            c[right] = temp
    c[left], c[pivot] = c[pivot], c[left]
    ## tell where the pivot is now
    return left

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
    print("Quick Sort [25, 65, 897, 23, 765,1234, 897, 23, 67]")
    tc1 = [25, 65, 897, 23, 765,1234, 897, 23, 67]
    quickSort(tc1)
    print(tc1)
    print("Quick Sort [-1, 1, 3]")
    tc2 = [-1, 1, 3]
    quickSort(tc2)
    print(tc2)
    print("=" * 100)
    print("Binary Tree Traversal")
    print("Preorder")
    tc1 = trees.BinaryTree('a')
    tc1.insertLeft('c')
    tc1.insertLeft('b')
    tc1.insertRight('e')
    tc1.insertRight('d')
    # print(tc1.getLeftChild().getRootVal())
    tc1.preorder()
    print("=" * 100)
    print("Inorder")
    tc1.inorder()
    print("=" * 100)
    print("Postorder")
    tc1.postorder()
    print("=" * 100)
    print("Graph")
    vt1 = graph.Vertex("Vert A")
    vt1.addNeighbor(graph.Vertex("Vert B"))
    print(vt1)
    print("=" * 100)
    g1 = graph.Graph()
    g1.addEdge("Vert A", "Vert B")
    for vert in g1:
        print(vert)
    print(g1.getVertices())


if __name__ == "__main__":
    main()
