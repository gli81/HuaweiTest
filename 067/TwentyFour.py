# -*- coding: utf-8 -*-

class TwentyFour:
    def twentyFour(self, nums: "list[int]", target: "int") -> "bool":
        if len(nums) == 1:
            return nums[0] == target
        else:
            for i in range(len(nums)):
                m = nums[0 : i] + nums[i + 1 :]
                n = nums[i]
                if self.twentyFour(m, target - n) or self.twentyFour(m, target + n) or\
                    self.twentyFour(m, target / n) or self.twentyFour(m, target * n):
                    return True
        return False


def main():
    test = TwentyFour()
    print(test.twentyFour([7, 2, 1, 10], 24))

if __name__ == "__main__":
    main()