# -*- coding: utf-8 -*-

class Chorus():
    def chorusDP(self, heights: 'list[int]') -> 'int':
        left_dp = self.dp(heights)
        right_dp = self.dp(heights[::-1])[::-1]
        # print(left_dp)
        # print(right_dp)
        overall_dp = []
        for i in range(len(left_dp)):
            overall_dp.append(left_dp[i] + right_dp[i] + 1)
        # print(overall_dp)
        return len(heights) - max(overall_dp)
    def dp(self, heights: 'list[int]') -> 'list[int]':
        dp = [0] * len(heights)
        for i in range(1, len(dp)):
            for j in range(i):
                if heights[i] > heights[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return dp

def main():
    test = Chorus()
    # print(test.dp([186, 186, 150, 200, 160, 130, 197, 200]))
    print(test.chorusDP([186, 186, 150, 200, 160, 130, 197, 200]))
    test_case_2 = "16 103 132 23 211 75 155 82 32 48 79 183 13 91 51 172 109 102 189 121 12 120 116 133 79 120 116 208 47 110 65 187 69 143 140 173 203 35 184 49 245 50 179 63 204 34 218 11 205 100 90 19 145 203 203 215 72 108 58 198 95 116 125 235 156 133 220 236 125 29 235 170 130 165 155 54 127 128 204 62 59 226 233 245 46 3 14 108 37 94 52 97 159 190 143 67 24 204 39 222 245 233 11 80 166 39 224 12 38 13 85 21 47 25 180 219 140 201 11 42 110 209 77 136".split()
    test_case_2 = list(map(int, test_case_2))
    print(test.chorusDP(test_case_2))

if __name__ == "__main__":
    main()