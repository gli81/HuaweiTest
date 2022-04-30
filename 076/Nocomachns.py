# -*- coding: utf-8 -*-

class Nocomachns:
    def nocomachns(self, n: "int") -> "list[int]":
        first = (n - 1) * (n - 1) + n
        ans = [first, ]
        for i in range(n - 1):
            ans.append(ans[i] + 2)
        return ans

def main():
    test = Nocomachns()
    print(1 ** 3, test.nocomachns(1))
    print(2**3, test.nocomachns(2))
    print(3**3, test.nocomachns(3))
    print(4**3, test.nocomachns(4))
    print(5**3, test.nocomachns(5))
    print(6**3, test.nocomachns(6))

if __name__ == "__main__":
    main()