# -*- coding: utf-8 -*-

class NumDay:
    def numDay(self, date: "str") -> "int":
        ans = 0
        [year, month, day] = list(map(int, date.split(" ")))
        to = [1, 3, 5, 7, 8, 10, 12]
        for m in range(1, month):
            if m in to:
                ans += 31
            elif m == 2:
                ans += 28
            else:
                ans += 30
        ans += day
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            if month > 2:
                ans += 1
        return ans

def main():
    test = NumDay()
    print(test.numDay("1982 3 4"))
    print(test.numDay("2012 12 31"))

if __name__ == "__main__":
    main()