# -*- coding: utf-8 -*-

import collections

class Maze():
    def maze(self, m: 'list[list[str]]', pre: 'list[list[tuple]]', end_x: 'int', end_y: 'int') -> 'list[list[tuple]]':
        ## working in the mathematical coordinate, not in the collection coordinate
        q = collections.deque([(end_x, end_y)])
        d = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        pre[end_y][end_x] = (0, 0)
        while q:
            x,y = q.popleft()
            for i in range(4):
                a, b = x + d[i][0], y + d[i][1]
                if a < 0 or a >= len(m[0]) or b < 0 or b >= len(m): ## out of bound
                    continue
                if m[b][a] == 1: ## obstacle
                    # print((a, b))
                    continue
                if pre[b][a][0] != -1: ## someone else has been here with a shorter path
                    ## for each step, go one tile forward.
                    ## So if this place has been reached before, it has to be reached with fewer steps
                    continue
                q.append((a, b))
                pre[b][a] = (x, y)
        return pre



def main():
    test = Maze()
    pre = [[(-1, -1)] * 5 for _ in range(5)]
    rslt = test.maze(
        [[0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]], pre, 4, 4
    )
    for i in rslt: print(i)
    x, y = 0, 0
    while True:
        print((x, y))
        if x == 4 and y == 4: break
        x, y = rslt[y][x][0], rslt[y][x][1]

if __name__ == "__main__":
    main()