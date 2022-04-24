# -*- coding: utf-8 -*-

class ConcatStr():
    def concatStr(self, str1: 'str', str2: 'str') -> 'str':
        ans = ''
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
        # print(second_step)
        for char in second_step:
            # print(self.hex2Bin(char))
            if char.isdigit() or (char.isalpha() and char.upper() < 'G'):
                ans += self.bin2Hex(self.hex2Bin(char)[::-1])
            else:
                ans += char
        return ans

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
        dec_form = self.bin2Dec(num)
        if dec_form < 10:
            return str(dec_form)
        else:
            return dec_hex_dict[dec_form]

    def bin2Dec(self, num: 'str') -> 'int':
        ans = 0
        for i in range(len(num)):
            ans += int(num[len(num) - i - 1]) * 2 ** i
        return ans

def main():
    test = ConcatStr()
    print(test.concatStr("dec", "fab"))
    print(test.concatStr("deca", "fab"))
    print(test.concatStr("Eqr", "v9oEb12U2ur4xu7rd931G1f50qDo"))
    ## test decimal to binary
    # print(test.dec2Bin(12))
    # print(test.dec2Bin(1))
    # print(test.dec2Bin(0))
    # print(test.dec2Bin(15))
    # print(test.dec2Bin(16))
    ## test hexadecimal to binary
    # print(test.hex2Bin("A"))
    # print(test.hex2Bin("b"))
    # print(test.hex2Bin("9"))
    # print(test.hex2Bin("f"))
    # print(test.hex2Bin("0"))
    ## test binary to decimal
    # print(test.bin2Dec("0000"))
    # print(test.bin2Dec("0001"))
    # print(test.bin2Dec("0101"))
    # print(test.bin2Dec("1111"))
    # print(test.bin2Dec("1100"))
    ## test binary to hexadecimal
    # print(test.bin2Hex("0000"))
    # print(test.bin2Hex("0001"))
    # print(test.bin2Hex("0101"))
    # print(test.bin2Hex("1111"))
    # print(test.bin2Hex("1100"))


if __name__ == "__main__":
    main()