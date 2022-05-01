# -*- coding: utf-8 -*-

class Egyptian:
    def egyptian(self, num: "str"):
        a,b = map(int,num.split('/'))

        while a > 1 and b % a == 0:
            b = int(b / a)
            a = int(a / a)
        # print((a, b))
        denom = 1
        ans=''
        while a != 0:
            print(denom)
            if a / b >= 1 / denom:
                ## [(a * denom) - b] / (b * denom)
                a = a * denom - b
                b = b * denom
                ans += f'1/{denom}+'
                # while a > 1 and b % a == 0:
                #     b = int(b / a)
                #     a = int(a / a)
                while a % 2 == 0 and b % 2 == 0:
                    a = int(a / 2)
                    b = int(b / 2)
                for n in range(3, b, 2):
                    if a % n == 0 and b % n == 0:
                        b = int(b / n)
                        a = int(a / n)
                print(ans)
            denom += 1
        return ans[:-1]
    
    def egyptian2(self, num: "str") -> "str":
        pass

def main():
    test = Egyptian()
    print(test.egyptian("8/11"))
    print(test.egyptian("2/4"))
    print(test.egyptian("17/73"))

if __name__ == "__main__":
    main()