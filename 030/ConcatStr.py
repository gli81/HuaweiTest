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
        print(second_step)
    def Hex2Bin(self, num: 'str') -> 'str':
        ans = ''
        hex_dec_dict = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15,\
            'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
        if num.isdigit():
            pass
    def Dec2Bin(self, num: 'int') -> 'str':
        ans = ''
        while num >= 1:
            if num % 2 == 1:
                ct += 1
            num = num // 2
        return ct

def main():
    test = ConcatStr()
    print(test.concatStr("dec", "fab"))
    print(test.concatStr("deca", "fab"))


if __name__ == "__main__":
    main()