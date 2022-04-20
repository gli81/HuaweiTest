# -*- coding: utf-8 -*-

class UniqueNum:
    def uniqueNum(self, num:'int') -> 'int':
        num = str(num)
        ans_list = []
        for i in range(len(num)):
            if num[len(num) - i -1] not in ans_list:
                ans_list.append(num[len(num) - i -1])
        ans = 0
        for i in range(len(ans_list)):
            ans += int(ans_list[i]) * 10 ** (len(ans_list) - i - 1)
        return ans

def main():
    test = UniqueNum()
    print(test.uniqueNum(9876673))

if __name__ == '__main__':
    main()
