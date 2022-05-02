# -*- coding: utf-8 -*-

class Number:
    def number(self, num: "str") -> "str":
        ans = ''
        for i in range(len(num)):
            if i == 0:
                if num[i].isdigit():
                    ans += '*'
                    ans += num[i]
                    if not num[i + 1].isdigit():
                        ans += '*'
                else:
                    ans += num[i]
            elif i == len(num) - 1:
                if num[i].isdigit():
                    if not num[i - 1].isdigit():
                        ans += '*'
                    ans += num[i]
                    ans += '*'
                else: ans += num[i]
            else:
                if num[i].isdigit() and not num[i - 1].isdigit():
                    ans += '*'
                ans += num[i]
                if num[i].isdigit() and not num[i + 1].isdigit():
                    ans += '*'
        return ans
def main():
    test = Number()
    print(test.number("Jkdi234klowe90a3"))

if __name__ == "__main__":
    main()
