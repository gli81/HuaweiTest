# -*- coding: utf-8 -*-

class ReverseNum:
    def reverseNum(self, num:'int')->'str':
        strNum = str(num)
        reversedStr = ""
        for i in range(len(strNum)):
            reversedStr += strNum[len(strNum)- i - 1]
        return reversedStr

def main():
    test = ReverseNum()
    print(test.reverseNum(1516000))

if __name__ == '__main__':
    main()