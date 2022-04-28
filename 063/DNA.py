# -*- coding: utf-8 -*-

class DNA:
    def dna(self, line: "str", num: "int") -> "str":
        ans = line
        hi: "float" = 0.0
        for i in range(len(line) - num):
            cur = self.CGRatio(line[i : i + num])
            if cur > hi:
                hi = cur
                ans = line[i : i + num]
        return ans

    def CGRatio(self, word: "str") -> "float":
        ct = 0
        for char in word:
            if char in "CG":
                ct += 1
        return ct / len(word)

def main():
    test = DNA()
    print(test.dna("ACGT", 2))
    print(test.dna("AACTGTGCACGACCTGA", 5))
    print(len("CCCAAGTCTTCCAATCGTGCCCCCCAATTGAGTCTCGCTCCCCAGGTGAGATACATCAGAAGC"))

if __name__ == "__main__":
    main()
