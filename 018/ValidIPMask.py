# -*- coding: utf-8 -*-

class ValidIPMask():
    def validIPMask(self, line: 'str') -> 'str':
        ## split, get IP and mask
        [ip, mask] = line.split('~')
        ip = list(map(int, ip.split('.')))
        mask = list(map(int, mask.split('.')))
        mask_str = ''.join(list(map(self.decimal2Binary, mask)))
        # print(ip)
        # print(self.validMask(mask_str))
        if self.validMask(mask_str):
            ## valid mask, check IP then
            pass
        else:
            return "invalid"

    def decimal2Binary(self, num: 'int') -> 'str':
        ans = ''
        if num == 0: return "0"
        while num > 0:
            if num % 2 == 1:
                ans += '1'
            else:
                ans += '0'
            num = num // 2
        return '0' * (8-len(ans)) + ans[::-1]
    def validMask(self, mask: 'str'):
        if mask[0] == '0': return False
        first_zero_index = -1
        for i in range(len(mask)):
            if mask[i] == '0':
                first_zero_index = i
                break
        if first_zero_index == -1: return False
        for char in mask[first_zero_index + 1 : len(mask)]:
            if char == '1': return False
        return True



def main():
    test = ValidIPMask()
    # print(test.decimal2Binary(64))
    # print(test.decimal2Binary(66))
    # print(test.decimal2Binary(22))
    # print(test.decimal2Binary(88))
    print(test.validIPMask("0.201.56.50~255.255.111.255"))
    # print(test.decimal2Binary(64 ^ 66))
    # print(test.validMask("11111111111111111111111100000000"))

if __name__ == "__main__":
    main()