# -*- coding: utf-8 -*-

class Seven():
    def seven(self, n: "int") -> "int":
        ans = 0
        for i in range(1, n + 1):
            if '7' in str(i) or i % 7 == 0:
                ans += 1
        return ans
        
def main():
    test = Seven()
    print(test.seven(20))

if __name__ == "__main__":
    main()