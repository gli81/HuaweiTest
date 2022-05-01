# -*- coding: utf-8 -*-

class LongestNum:
    def longestNum(self, line: "str") -> "str":
        anss = []
        l = 0
        i = 0
        while i < len(line):
            if line[i].isdigit():
                ct = 1
                if ct >= l: ## first number
                    anss.append(line[i])
                    l = ct
                for j in range(i + 2, len(line) + 1):
                    if line[i:j].isdigit():
                        ct += 1
                        if ct > l:
                            anss.clear()
                            anss.append(line[i:j])
                            l = ct
                        elif ct == l:
                            anss.append(line[i:j])
                        if j == len(line):
                            i = j
                            break
                    else:
                        i = j
                        break
                if i == len(line) - 1:
                    if l == 1 and line[-1].isdigit():
                        anss.append(line[-1])
                        i += 1
                    else:
                        i += 1
            else:
                i += 1
        return anss, l

def main():
    test = LongestNum()
    print(test.longestNum("abcd12345ed125ss123058789"))
    # print(test.longestNum("abcd12345ed125ss123058789a"))
    print(test.longestNum("a8a72a6a5yy98y65ee1r2"))

if __name__ == "__main__":
    main()