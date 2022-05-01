# -*- coding: utf-8 -*-

class Redraiment:
    def redraiment(self, nums: "list[int]") -> "int":
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            # print(dp)
        return max(dp)
        
def main():
    test = Redraiment()
    print(test.redraiment([2, 5, 1, 5, 4, 5]))
    print(test.redraiment([237, 153, 196, 160, 154, 91, 195, 250, 129, 219, 14, 29, 209]))

if __name__ == "__main__":
    main()