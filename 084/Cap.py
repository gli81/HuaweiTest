# -*- coding: utf-8 -*-

class Cap:
    def cap(self, line: "str") -> "int":
        ct = 0
        for letter in line:
            if letter.isupper():
                ct += 1
        return ct

def main():
    test = Cap()
    print(test.cap("A 1 0 1 1150175017(&^%&$vabovbaoadd 123#$\%\#%#O"))

if __name__ == "__main__":
    main()
