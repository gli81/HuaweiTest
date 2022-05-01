# -*- coding: utf-8 -*-

class Square:
    def square(self, n: "int", m: "int") -> "int":
        '''
        go right n times, go down m times
        for i th step in the total n + m steps
        either right or down, choose n right steps from n + m steps
        6 steps total, 2 hor, 4 ver
        1 2 3 4 5 6
        1 2 selected same as 2 1 selected
        so combination (order doesn't matter)
        (m + n)! / (m!n!)
        '''
        return int(self.factorial(m + n) / (self.factorial(m) * self.factorial(n)))

    def factorial(self, n: "int") -> "int":
        ans = 1
        for i in range(2, n + 1):
            ans *= i
        return ans

def main():
    test = Square()
    print(test.square(4, 2))
    print(test.factorial(4))
    print(test.factorial(0))
    print(test.factorial(1))

if __name__ == "__main__":
    main()
