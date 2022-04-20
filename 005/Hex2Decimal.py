# -*- coding: utf-8 -*-

class Hex2Decimal:
    def hexConvert(self, num: str) -> int:
        converter = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
        ans = 0
        num = num[2:]## get rid of 0x
        for i in range(len(num)):
            if num[len(num) - i - 1] in converter:
                ans += converter[num[len(num) - i - 1]] * 16 ** i
            else:
                ans += int(num[len(num) - i - 1]) * 16 ** i
        return ans

def main():
    test = Hex2Decimal()
    print(test.hexConvert("0x2C"))

if __name__ == '__main__':
    main()
