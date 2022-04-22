# -*- coding: utf-8 -*-

from unittest import case


class SortStr():
    def sortStr(self, line: 'str') -> 'str':
        to_be_sorted = []
        cap = []
        ans = ['_'] * len(line)
        for index in range(len(line)):
            if line[index].islower():
                to_be_sorted.append(line[index].upper())
                cap.append(0)
            elif line[index].isupper():
                to_be_sorted.append(line[index])
                cap.append(1)
            else:
                ans[index] = line[index]
        ## use a bubble sort to sort letters and their cases
        # print(to_be_sorted)
        # print(cap)
        for i in range(len(to_be_sorted) - 1):
            for j in range(len(to_be_sorted) - i - 1):
                if ord(to_be_sorted[j]) > ord(to_be_sorted[j + 1]):
                    temp = to_be_sorted[j]
                    to_be_sorted[j] = to_be_sorted[j + 1]
                    to_be_sorted[j + 1] = temp
                    case_temp = cap[j]
                    cap[j] = cap[j + 1]
                    cap[j + 1] = case_temp
        ## change back the cases
        for i in range(len(cap)):
            if cap[i] == 0:
                to_be_sorted[i] = to_be_sorted[i].lower()
        # print(to_be_sorted)
        # print(cap)
        ans = ''.join(ans)
        for char in to_be_sorted:
            ans = ans.replace('_', char, 1)
        return ans
        

def main():
    test = SortStr()
    print(test.sortStr("A Famous Saying: Much Ado About Nothing (2012/8)."))
    # print(sorted(list("A Famous Saying: Much Ado About Nothing (2012/8).")))

if __name__ == "__main__":
    main()
