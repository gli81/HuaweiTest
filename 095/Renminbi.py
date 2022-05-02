# -*- coding: utf-8 -*-

class Renminbi:
    def renminbi(self, num: "double") -> "str":
        ch = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
        ans = ''
        ## deal with decimal
        if num - int(num) == 0:
            ans = ans + "元整"
        else:
            if num * 100 % 10 != 0:
                ans = ans + ch[int(num * 100 % 10)] + '分'
            num = num - (num * 100 % 10) / 100
            if num * 10 % 10 != 0:
                ans = ch[int(num * 10 % 10)] + '角' + ans
        num = int(num)
        
        return ans

def main():
    test = Renminbi()
    print(test.renminbi(151121.15))
    print(test.renminbi(1010.00))

if __name__ == "__main__":
    main()
