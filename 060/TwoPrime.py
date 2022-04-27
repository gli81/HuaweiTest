# -*- coding: utf-8 -*-

class TwoPrime:
    def twoPrime(self, num:"int") -> "list[int]":
        diff = num + 1
        ans = [-1, -1]
        for i in range(2, int(num / 2)  + 1):
            if self.isPrime(i) and self.isPrime(num - i) and num - i - i < diff:
                diff = num - i - i
                ans = [i, num - i]
        return ans

    def isPrime(self, num: "int") -> "bool":
        if num < 3:
            return True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

def main():
    test = TwoPrime()
    print(test.twoPrime(20))
    print(test.twoPrime(4))
    # print(test.isPrime(2))
    # print(test.isPrime(3))
    # print(test.isPrime(4))
    # print(test.isPrime(5))
    # print(test.isPrime(6))
    # print(test.isPrime(11))

if __name__ == "__main__":
    main()