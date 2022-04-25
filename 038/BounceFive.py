# -*- coding: utf-8 -*-

class BounceFive():
    def bounceFive(self, height: 'int') -> 'tuple[int, int]':
        heights = [0] * 5
        heights[0] = float(height)
        for i in range(1, len(heights)):
            heights[i] = heights[i - 1] / 2
        return sum(heights) + sum(heights[1:]), heights[-1] / 2

def main():
    test = BounceFive()
    print(test.bounceFive(1))

if __name__ == "__main__":
    main()