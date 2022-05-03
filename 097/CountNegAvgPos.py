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
    print(test.countNegAvgPos([18259, 3386, -3490, 64453, -1571, 57543, 12151, 2186, -17851, 56212, 42919, 48020, -409, 13979, 49103, -4985, 28018, -13005, 21866, 48272, 17400, 76308, 49960, 22177, -19074, 40860, 35215, -1608, 69665, 70068, 1127, 16417, 42894, 36660, 66927, 24406, -8651, 34582, 57412, -5440, -2059, 26052, 11727, 68881, 30676, 19227, -13007, 67727, 13582, 72918, 66762, -15575, 25595, -8260, 68470, 75520, 10708]))

if __name__ == "__main__":
    main()
