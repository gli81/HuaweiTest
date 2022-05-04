# -*- coding: utf-8 -*-

import collections


def maze(maze: "list[list[int]]") -> "list[list[int]]":
    nrow = len(maze)
    ncol = len(maze[0])
    pre = [[(-1, -1)] * ncol for _ in range(nrow)]
    q = collections.deque([(nrow - 1, ncol - 1)])
    pre[nrow - 1][ncol - 1] = (0, 0)
    d = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    while q:
        x, y = q.popleft()
        for i in range(4):
            a, b = x + d[i][0], y + d[i][1]
            if a < 0 or a >= nrow or b < 0 or b >= ncol: ## out of bound
                continue
            if maze[a][b] == 1: ## blocked
                continue
            if pre[a][b][0] != -1: ## been here with shorter path
                continue
            q.append((a, b))
            pre[a][b] = (x, y)
        # print(q)
    return pre

def printResult(pre, x = 0, y = 0) -> "None":
    while True:
        print(f"({x}, {y})")
        if x == len(pre) - 1 and y == len(pre[0]) - 1: break
        x, y = pre[x][y]

def main():
    m1 = [
        [0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0]
    ]
    m2 = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    pre1 = maze(m1)
    printResult(pre1)
    print('-' * 50)
    pre2 = maze(m2)
    printResult(pre2)
    # print(pre2)

if __name__ == "__main__":
    main()
