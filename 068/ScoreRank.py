# -*- coding: utf-8 -*-

class ScoreRank:
    def scoreRank(self, order: "int", scores: "list[str]") -> "list[str]":
        score_list = [int(line.split()[1]) for line in scores]
        # print(scores)
        # print(score_list)
        self.quickSortHelper(score_list, scores, 0, len(scores) - 1)
        return scores if not order else scores[::-1]


    def quickSortHelper(self, alist: "list[int]", blist: "list[str]", first: "int", last: "int") -> "None":
        if first < last:
            splitPoint = self.partition(alist, blist, first, last)
            self.quickSortHelper(alist, blist, first, splitPoint - 1)
            self.quickSortHelper(alist, blist, splitPoint + 1, last)
            print(alist)

    def partition(self, alist: "list[int]", blist: "list[str]", first: "int", last: "int") -> "int":
        pivot = alist[first]
        pivotValue = blist[first]
        left = first
        right = last
        while left < right:
            while left < right and alist[right] >= pivot:
                right -= 1
            alist[left] = alist[right]
            blist[left] = blist[right]
            while left < right and alist[left] <= pivot:
                left += 1
            alist[right] = alist[left]
            blist[right] = blist[left]
        alist[left] = pivot
        blist[left] = pivotValue
        return left
        
def main():
    test = ScoreRank()
    # print(test.scoreRank(0, ["fang 90", "yang 50", "ning 70"]))
    # print(test.scoreRank(1, ["fang 90", "yang 50", "ning 70"]))
    # print(test.scoreRank(1, ["fang 4", "yang 7", "ning 72"]))
    print(test.scoreRank(1, ["fang 43", "yang 87", "ning 67"]))

if __name__ == "__main__":
    main()