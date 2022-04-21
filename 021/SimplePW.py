# -*- coding: utf-8 -*-

class SimplePW:
    def simplePassword(self, pw: 'str') -> 'str':
        ans = ""
        for i in pw:
            if i.islower():
                if i in ['a', 'b', 'c']:
                    ans += '2'
                if i in ['d', 'e', 'f']:
                    ans += '3'
                if i in ['g', 'h', 'i']:
                    ans += '4'
                if i in ['j', 'k', 'l']:
                    ans += '5'
                if i in ['m', 'n', 'o']:
                    ans += '6'
                if i in ['p', 'q', 'r', 's']:
                    ans += '7'
                if i in ['t', 'u', 'v']:
                    ans += '8'
                if i in ['w', 'x', 'y', 'z']:
                    ans += '9'
            elif 64 < ord(i) < 90:
                ans += chr(ord(i) + 33)
            elif i == 'Z':
                ans += 'a'
            else:
                ans += i
        return ans

def main():
    test = SimplePW()
    print(test.simplePassword("YUANzhi1987"))

if __name__ == "__main__":
    main()
