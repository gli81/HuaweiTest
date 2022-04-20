# -*- coding: utf-8 -*-

class CharAppearance:
    def charApperance(self, word:str, letter:str) -> int:
        ct = 0
        for l in word:
            if l.upper() == letter or l.lower == letter:
                ct += 1
        return ct

def main():
    test = CharAppearance()
    print(test.charApperance("ABCabc", "A"))

if __name__ == '__main__':
    main()