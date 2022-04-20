# -*- coding: utf-8 -*-

import math

class PrimeFactor:
    def primeFactor(self, num: 'int') -> 'list[int]':
        ans = []
        n = 2
        while n < (int(math.sqrt(num)) + 1):
            if num % n == 0:
                ans.append(n)
                num /= n
                n -= 1
            n += 1
        ans.append(int(num))
        return ans

def main():
    test = PrimeFactor()
    print(test.primeFactor(12))
    print(test.primeFactor(16))
    print(test.primeFactor(15))
    print(test.primeFactor(11))
    print(test.primeFactor(2))
    print(test.primeFactor(999))

if __name__ == '__main__':
    main()
