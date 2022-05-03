# -*- coding: utf-8 -*-

class LCM:
    def lcm(self, num1: "int", num2: "int") -> "int":
        if num1 > num2:
            num1, num2 = num2, num1
        done = False
        m = 0
        while not done:
            m += 1
            if m * num2 % num1 == 0:
                done = True
        return m * num2

def main():
    test = LCM()
    print(test.lcm(5, 7))
    print(test.lcm(4, 2))

if __name__ == "__main__":
    main()
