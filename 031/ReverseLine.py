# -*- coding: utf-8 -*-

class ReverseLine():
    def reverseLine(self, line: 'str'):
        for char in line:
            if not char.isalpha():
                line = line.replace(char, ' ', 1)
        splited = line.split()
        ans = ''
        for i in range(len(splited) - 1, -1, -1):
            ans += splited[i]
            if i != 0:
                ans += ' '
        return ans

def main():
    test = ReverseLine()
    print(test.reverseLine("I am a student"))
    print(test.reverseLine("$bo*y gi!r#l"))

if __name__ == "__main__":
    main()