# -*- coding: utf-8 -*-

class VerifyPW:
    def verifyPW(self, pws: 'list[str]') -> 'list[str]':
        ans = []
        for pw in pws:
            len_flag = False
            if len(pw) > 8: len_flag = True
            a = b = c = d = 0
            for letter in pw:
                if letter.isdigit():
                    a = 1
                elif letter.islower():
                    b = 1
                elif letter.isupper():
                    c = 1
                else: d = 1
            if len_flag and a + b + c + d > 2 and not self.repeatSubstring(pw):
                ans.append("OK")
            else: ans.append("NG")
        return ans
    def repeatSubstring(self, line: 'str') -> 'bool':
        substring = []
        for i in range(len(line) - 2):
            check = line[i : i + 3]
            # print(check)
            if check in substring[:-2]: return True
            else: substring.append(check)
        return False

def main():
    test = VerifyPW()
    print(test.verifyPW(["021Abc9000", "021Abc9Abc1", "021ABC9000", "021$bc9000", "aAAAAA&bbvn"]))

if __name__ == "__main__":
    main()
