# -*- coding: utf-8 -*-

class Decimal2Binary:
    def decimal2Binary(self, num:'int') -> 'int':
        digits = []
        while num >= 1:
            digits.append(num % 2)
            num = num // 2
        ct = 0
        for digit in digits:
            if digit == 1:
                ct += 1
        return ct

def main():
    test = Decimal2Binary()
    print(test.decimal2Binary(5))
    print(test.decimal2Binary(0))
    print(test.decimal2Binary(11))

if __name__ == '__main__':
    main()