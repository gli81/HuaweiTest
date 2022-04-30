# -*- coding: utf-8 -*-

class CommonSubstring:
    def commonSubstring(self, s1: "str", s2: "str") -> "str":
        ans = 0
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        for i in range(len(s1)):
            for j in range(i, len(s1) + 1):
                if s1[i:j] in s2 and j - i > ans:
                    ans = j - i
        return ans

def main():
    test = CommonSubstring()
    print(test.commonSubstring("asdfas", "werasdfaswer"))

if __name__ == "__main__":
    main()