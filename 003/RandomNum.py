# -*- coding: utf-8 -*-

class RandomNum:
    def randomNum(self, *args:int) -> list[int]:
        input_nums = list(args)
        # return input_nums.sort()
        ans = []
        for i in input_nums:
            if i not in ans:
                ans.append(i)
        return sorted(ans)

def main():
    test = RandomNum()
    print(test.randomNum(2, 2, 1))

if __name__ == '__main__':
    main()