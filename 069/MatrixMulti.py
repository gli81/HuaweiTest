# -*- coding: utf-8 -*-

class MatrixMulti:
    def matrixMulti(self, m1: "int", n1: "int", n2: "int", *line) -> "list[list[int]]":
        mat1 = []
        mat2 = []
        for i in range(m1):
            mat1.append(line[i])
        for i in range(m1, m1 + n1):
            mat2.append(line[i])
        # print(mat1)
        # print(mat2)
        mat2_t = []
        for i in range(n2):
            cur = []
            for j in range(n1):
                cur.append(mat2[j][i])
            mat2_t.append(cur)
        # print(mat2_t)
        ans = []
        for i in range(m1):
            cur = []
            for j in range(n2):
                tile = 0
                for k in range(n1):
                    tile += mat2_t[j][k] * mat1[i][k]
                cur.append(tile)
            ans.append(cur)
        print(ans)
def main():
    test = MatrixMulti()
    print(test.matrixMulti(2, 3, 2, [1, 2, 3], [3, 2, 1], [1, 2], [2, 1], [3, 3]))
    print(test.matrixMulti(2, 3, 3, [1, 2, 3], [3, 2, 1], [1, 2, 3], [2, 1, 3], [3, 3, 3]))

if __name__ == "__main__":
    main()
