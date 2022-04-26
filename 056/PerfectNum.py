# -*- coding: utf-8 -*-

class PerfectNum():
    def perfectNum(self, num: "int") -> "int":
        ct = 0
        # ans = []
        for i in range(2, num + 1):
            sum_ = 1
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    sum_ += j
                    sum_ += i / j
            if i == sum_:
                ct += 1
                # ans.append(i)
        # print(ans)
        return ct

def main():
    test = PerfectNum()
    print(test.perfectNum(1000))

if __name__ == "__main__":
    main()