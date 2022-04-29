# -*- coding: utf-8 -*-

class MatrixMultiLoad:
    def matrixMultiLoad(self, num: "int", order: "str", *lines) -> "int":

        pass

    def loadForTwo(self, dim1: "list[int]", dim2: "list[int]") -> "int":
        return dim1[0] * dim1[1] * dim2[1]

def main():
    test = MatrixMultiLoad()
    print(test.matrixMultiLoad(3, "(A(BC))", [50, 10], [10, 20], [20, 5]))
    print(test.loadForTwo([50, 10], [10, 20]))

if __name__ == "__main__":
    main()
