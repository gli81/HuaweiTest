# -*- coding: utf-8 -*-

class RabbitNum():
    def rabbitNum(self, n: 'int') -> 'int':
        if n < 3:
            return 1
        else:
            return self.rabbitNum(n - 2) + self.rabbitNum(n - 1)

def main():
    test = RabbitNum()
    print(test.rabbitNum(3))
    print(test.rabbitNum(31))

if __name__ == "__main__":
    main()