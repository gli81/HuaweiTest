# -*- coding: utf-8 -*-

class IntergerIP():
    def integer2IP(self, num: 'str') -> 'str':
        b = self.dec2Bin(int(num), True)
        return '.'.join(list(map(str, map(self.bin2Dec, [b[0:8], b[8:16], b[16:24], b[24:32]]))))

    def ip2Integer(self, ip: 'str') -> 'str':
        pass

    def dec2Bin(self, num: 'int', long: 'bool' = False) -> 'str':
        ans = ''
        if num == 0: ans = "00000000"
        while num > 0:
            if num % 2 == 1:
                ans += '1'
            else:
                ans += '0'
            num = num // 2
        if len(ans) < 8: ans = ans + '0' * (8 - len(ans))
        if len(ans) < 32 and long: ans = ans + '0' * (32 - len(ans))
        return ans[::-1]

    def bin2Dec(self, num: 'str') -> 'int':
        ans = 0
        for i in range(len(num)):
            ans += int(num[len(num) - i - 1]) * 2 ** i
        return ans

def main():
    test = IntergerIP()
    print(test.integer2IP('167773121'))
    # print(test.dec2Bin(255))
    # print(test.dec2Bin(0))
    # print(test.dec2Bin(252))

if __name__ == "__main__":
    main()