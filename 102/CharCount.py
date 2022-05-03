# -*- coding: utf-8 -*-

import string

class CharCount:
    def charCount(self, line: "str") -> "str":
        temp = dict()
        for char in line:
            temp[char] = temp.get(char, 0) + 1
        # print(temp)
        maxx = max(temp.values())
        # print(maxx)
        ans = ''
        while maxx > 0:
            for char in string.digits:
                if temp.get(char, 0) == maxx:
                    ans += char
            for char in string.ascii_lowercase:
                if temp.get(char, 0) == maxx:
                    ans += char
            maxx -= 1
        return ans

def main():
    test = CharCount()
    print(test.charCount("aaddccdc"))
    print(test.charCount("6uym66c0l609vb6mg75q90zyf9d4styi257709"))

if __name__ == "__main__":
    main()
