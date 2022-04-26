# -*- coding: utf-8 -*-

class Triangle():
    def triangle(self, n: "int") -> "int":
        ## -1 -1 2 3 2 4 2 3 2 4...
        if n < 3: return -1
        return [2, 3, 2, 4][(n - 3) % 4]

def main():
    test = Triangle()
    print(test.triangle(3))
    print(test.triangle(4))
    print(test.triangle(5))
    print(test.triangle(6))
    print(test.triangle(7))

if __name__ == "__main__":
    main()