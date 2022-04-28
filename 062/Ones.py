# -*- coding: utf-8 -*-

class Ones:
    def ones(self, num: "int") -> "int":
        ct = 0
        for i in self.dec2Bin(num):
            if i == '1':
                ct += 1
        return ct

    def dec2Bin(self, num: "int") -> "str":
        if num == 0:
            return '0'
        ans = ''
        while num > 0:
            if num % 2 == 0:
                ans = '0' + ans
            else:
                ans = '1' + ans
            num = num // 2
        return ans

def main():
    test = Ones()
    print(test.dec2Bin(2))
    print(test.dec2Bin(1))
    print(test.dec2Bin(16))
    print(test.dec2Bin(15))
    print(test.ones(2))
    print(test.ones(1))
    print(test.ones(16))
    print(test.ones(15))

if __name__ == "__main__":
    main()