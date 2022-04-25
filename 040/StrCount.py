# -*- coding: utf-8 -*-

class StrCount():
    def strCount(self, line:'str') -> 'list[int]':
        ct = [0] * 4
        for char in line:
            if char.isalpha():
                ct[0] += 1
            elif char == ' ':
                ct[1] += 1
            elif char.isdigit():
                ct[2] += 1
            else:
                ct[3] += 1
        return ct

def main():
    test = StrCount()
    print(test.strCount("1qazxsw23 edcvfr45tgbn hy67uj m,ki89ol.\\\\/;p0-=\\\\]["))

if __name__ == "__main__":
    main()