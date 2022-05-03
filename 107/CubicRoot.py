# -*- coding: utf-8 -*-

class CubicRoot:
    def cubicRoot(self, num: "float", epsilon: "float" = 0.001) -> "float":
        if num == 0: return 0
        if num > 0: sign = 1
        if num < 0: sign = -1
        num = abs(num)
        if num > 1:
            start = 0
            end = num
        else:
            start = num
            end = 1
        mid = (end + start) / 2
        while abs(mid ** 3 - num) > epsilon:
            if mid ** 3 > num:
                end = mid
            else:
                start = mid
            mid = (start + end) / 2
        return round(sign * mid, 1)

def main():
    test = CubicRoot()
    print(test.cubicRoot(19.9))
    print(test.cubicRoot(2.7))

if __name__ == "__main__":
    main()