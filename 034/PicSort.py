# -*- coding: utf-8 -*-

class PicSort():
    def picSort(self, line: 'str') -> 'str':
        return ''.join(sorted(line))

def main():
    test = PicSort()
    print(test.picSort("Ihave1nose2hands10fingers"))

if __name__ == "__main__":
    main()