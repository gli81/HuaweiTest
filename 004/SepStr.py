# -*- coding: utf-8 -*-

class SepStr:
    def sepStr(self, line: str) -> None:
        while len(line) % 8 != 0:
            line = line + '0'
        for i in range(len(line)):
            if i % 8 == 0:
                print()
            print(line[i], end='')

def main():
    test = SepStr()
    test.sepStr("abcabcabc")

if __name__ == '__main__':
    main()