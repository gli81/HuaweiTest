# -*- coding: utf-8 -*-

class CountNegAvgPos:
    def countNegAvgPos(self, nums: "list[int]") -> "tuple[int, float]":
        total_pos = 0.0
        ct_pos = 0.0
        ct = 0
        for i in nums:
            if i > 0:
                ct_pos += 1
                total_pos += i
            elif i < 0:
                ct += 1
        ans_avg = round(total_pos / ct_pos, 1) if not ct_pos == 0 else 0.0
        return ct, ans_avg

def main():
    test = CountNegAvgPos()
    print(test.countNegAvgPos([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, -1]))

if __name__ == "__main__":
    main()
