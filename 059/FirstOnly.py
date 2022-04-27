# -*- coding: utf-8 -*-

class FirstOnly:
    def firstOnly(self, line: "str") -> "str":
        lst1 = []
        lst2 = []

        for char in line:
            if char in lst1 and char not in lst2:
                lst2.append(char)
            lst1.append(char)
        flag = False
        for char in line:
            if char not in lst2:
                return(char)
                flag = True
                break
        if not flag:
            return "-1"

def main():
    test = FirstOnly()
    print(test.firstOnly("asdfasdfo"))
    print(test.firstOnly("asdfasdfoo"))

if __name__ == "__main__":
    main()