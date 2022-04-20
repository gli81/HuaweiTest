# -*- coding: utf-8 -*-

class Approx:
    def approx(self, num:'float'):
        deci_part = num - int(num)
        return int(num) + 1 if deci_part >= 0.5 else int(num)

def main():
    test = Approx()
    print(test.approx(5.5))
    print(test.approx(2.499))

if __name__ == '__main__':
    main()