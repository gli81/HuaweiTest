# -*- coding: utf-8 -*-

class MatrixMultiLoad:
    def matrixMultiLoad(self, num: "int", order: "str", *lines) -> "int":
        # print(lines)
        mats = list(lines)
        # print(mats)
        stk = []
        ans = 0
        for char in order:
            if char == '(':
                stk.append(char)
            elif char.isalpha():
                stk.append(mats.pop(0))
            elif char == ')':
                b = stk.pop()
                a = stk.pop()
                stk.pop()
                ans += self.loadForTwo(a, b)
                stk.append([a[0], b[1]])
        return ans

    def loadForTwo(self, dim1: "list[int]", dim2: "list[int]") -> "int":
        return dim1[0] * dim1[1] * dim2[1]

def main():
    test = MatrixMultiLoad()
    print(test.matrixMultiLoad(3, "(A(BC))", [50, 10], [10, 20], [20, 5]))
    print(test.matrixMultiLoad(3, "((AB)C)", [50, 10], [10, 20], [20, 5]))
    print(test.loadForTwo([50, 10], [10, 20]))

if __name__ == "__main__":
    main()
