# -*- coding: utf-8 -*-

class ValidIPMask():
    def validIPMask(self, line: 'str') -> 'bool':
        ## split, get IP and mask
        [ip, mask] = line.split('~')
        ip = list(map(int, ip.split('.')))
        mask = list(map(int, mask.split('.')))
        mask_str = ''.join(list(map(self.decimal2Binary, mask)))
        print(ip)
        print(mask_str)
    def decimal2Binary(self, num: 'int') -> 'str':
        ans = ''
        if num == 0: return "0"
        while num > 0:
            if num % 2 == 1:
                ans += '1'
            else:
                ans += '0'
            num = num // 2
        return ans[::-1]


def main():
    test = ValidIPMask()
    print(test.decimal2Binary(64))
    print(test.decimal2Binary(66))
    # print(test.decimal2Binary(22))
    # print(test.decimal2Binary(88))
    print(test.validIPMask("0.201.56.50~255.255.111.255"))
    print(test.decimal2Binary(64 ^ 66))

if __name__ == "__main__":
    main()