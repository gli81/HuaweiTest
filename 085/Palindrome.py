# -*- coding: utf-8 -*-

class Palindrome:
    def palindrome(self, line: "str") -> "int":
        ans = 1
        for i in range(len(line)):
            for j in range(i + 1, len(line) + 1):
                if self.isPal(line[i:j]):
                    if j - i > ans:
                        ans = j - i
        return ans

    def isPal(self, word: "str") -> "bool":
        if len(word) <= 1: return True
        return word[0] == word[-1] and self.isPal(word[1:-1])

def main():
    test = Palindrome()
    print(test.palindrome("cdabbacc"))
    print(test.palindrome("abba"))
    # print(test.isPal("c"))
    # print(test.isPal("cc"))

if __name__ == "__main__":
    main()