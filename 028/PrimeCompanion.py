# -*- coding: utf-8 -*-

class PrimeCompanion():
    def primeCompanion(self, nums: 'list[int]') -> 'int':
        evens = []
        odds = []
        for num in nums:
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)
        ct = 0
        for i in odds:
            pass
    def isPrime(self, num: 'int'):
        if num == 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

def main():
    test = PrimeCompanion()

if __name__ == "__main__":
    main()