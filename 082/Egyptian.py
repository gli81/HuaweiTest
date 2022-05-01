# -*- coding: utf-8 -*-

class Egyptian:
    def egyptian(self, num: "str"):
        a,b = map(int,num.split('/'))

        while a > 1 and b % a == 0:
            b = int(b / a)
            a = int(a / a)
        print((a, b))

def main():
    test = Egyptian()
    test.egyptian("8/11")
    test.egyptian("2/4")

if __name__ == "__main__":
    main()