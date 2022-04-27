# -*- coding: utf-8 -*-

class KSmallest():
    def kSmallest(self, nums: "list[int]", k: "int") -> "list[int]":
        return sorted(nums)[:k]

def main():
    test = KSmallest()
    print(test.kSmallest([1, 3, 5, 7, 2], 2))

if __name__ == "__main__":
    main()