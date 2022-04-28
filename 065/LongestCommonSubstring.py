# -*- coding: utf-8 -*-

class LongestCommonSubstring:
    def longestCommonSubstring(self, str1: "str", str2: "str") -> "str":
        flag = False
        if len(str1) > len(str2):
            str1, str2 = str2, str1
            flag = True
        ans_len = -1
        ans = ''
        for i in range(len(str1) - 1):
            for j in range(i + 2, len(str1) + 1):
                if str1[i:j] in str2:
                    if j - i > ans_len:
                        ans_len = j - i
                        ans = str1[i:j]
                else:
                    break
        if ans_len == -1:
            if flag:
                return str2[0]
            else:
                return str1[0]
        return ans

def main():
    test = LongestCommonSubstring()
    print(test.longestCommonSubstring("abcdefghijklmnop", "abcsafjklmnopqrstuvw"))

if __name__ == "__main__":
    main()
