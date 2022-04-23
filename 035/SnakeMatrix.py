# -*- coding: utf-8 -*-

class SnakeMatrix():
    def snakeMatrix(self, num: 'int') -> 'None':
        for i in range(num):
            out = [sum(range(i + 1)) + 1] * (num - i)
            for j in range(1, len(out)):
                # print(j, sum(range(j + 1)))
                out[j] = out[j - 1] + i + j + 1
                # pass
            print(' '.join(map(str, out)))

def main():
    test = SnakeMatrix()
    test.snakeMatrix(5)
    test.snakeMatrix(4)

if __name__ == "__main__":
    main()