# -*- coding: utf-8 -*-

class ConcatStr():
    def concatStr(self, str1: 'str', str2: 'str') -> 'str':
        first_step = str1 + str2
        odds = []
        evens = []
        for i in range(len(first_step)):
            if i % 2 == 0:
                evens.append(first_step[i])
            else:
                odds.append(first_step[i])
        second_step = ''
        [evens, odds] = list(map(sorted, [evens, odds]))
        if len(evens) > len(odds):
            odds.append('')
        # print(evens, odds)
        for i in range(len(evens)):
            second_step = second_step + evens[i] + odds[i]
        for char in second_step:
            print(self.hex2Bin(char))

    def hex2Bin(self, num: 'str') -> 'str':
        hex_dec_dict = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
        if num.isdigit():
            return self.dec2Bin(int(num))
        elif num.isalpha() and num.lower() in hex_dec_dict:
            return self.dec2Bin(hex_dec_dict[num.lower()])

    def dec2Bin(self, num: 'int') -> 'str':
        ans = ''
        if num == 0: ans = "0000"
        while num > 0:
            if num % 2 == 1:
                ans += '1'
            else:
                ans += '0'
            num = num // 2
        if len(ans) < 4: ans = ans + '0' * (4 - len(ans))
        return ans[::-1]

    def bin2Hex(self, num: 'str') -> 'str':
        dec_hex_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    def bin2Dec(self, num: 'str') -> 'int':
        pass

def main():
    test = ConcatStr()
    print(test.concatStr("dec", "fab"))
    print(test.concatStr("deca", "fab"))
    # print(test.dec2Bin(12))
    # print(test.dec2Bin(1))
    # print(test.dec2Bin(0))
    # print(test.dec2Bin(15))
    # print(test.dec2Bin(16))
    # print(test.hex2Bin("A"))
    # print(test.hex2Bin("b"))
    # print(test.hex2Bin("9"))
    # print(test.hex2Bin("f"))
    # print(test.hex2Bin("0"))


if __name__ == "__main__":
    main()