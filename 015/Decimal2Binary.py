# -*- coding: utf-8 -*-

class Decimal2Binary:
    def decimal2Binary(self, num:'int') -> 'int':
        ct = 0
        while num >= 1:
            if num % 2 == 1:
                ct += 1
            num = num // 2
        return ct

def main():
    test = Decimal2Binary()
    print(test.decimal2Binary(5))
    print(test.decimal2Binary(0))
    print(test.decimal2Binary(11))

if __name__ == '__main__':
    main()