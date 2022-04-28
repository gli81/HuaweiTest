# -*- coding: utf-8 -*-

class Apple:
    def apple(self, n: "int", np: "int") -> "int":
        if n <= 1 or np <= 1:
            return 1
        elif np > n:
            return self.apple(n, n)
        else:
            return self.apple(n, np - 1) + self.apple(n - np, np)

        

def main():
    test = Apple()
    print(test.apple(7, 3))
    print(test.apple(8, 3))

if __name__ == "__main__":
    main()