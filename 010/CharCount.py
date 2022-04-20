# -*- coding: utf-8 -*-

class CharCount:
    def charCount(self, chars:'str')->'int':
        appeared = []
        ct = 0
        for char in chars:
            if 0 <= ord(char) <= 127:
                if char not in appeared:
                    appeared.append(char)
                    ct += 1
        return ct

def main():
    test = CharCount()
    print(test.charCount("aaa"))
    print(test.charCount("abc"))

if __name__ == '__main__':
    main()