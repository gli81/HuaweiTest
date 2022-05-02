# -*- coding: utf-8 -*-

class Vote:
    def vote(self, candidate: "list[str]", v: "list[str]") -> "dict[str, int]":
        ans = {}
        for cand in candidate:
            ans[cand] = 0
        ans["Invalid"] = 0
        for i in v:
            if i in candidate:
                ans[i] += 1
            else:
                ans["Invalid"] += 1
        return ans

def main():
    test = Vote()
    print(test.vote(['A', 'B', 'C', 'D'], ['A', 'D', 'E', "CF", 'A', "GG", 'A', 'B']))

if __name__ == "__main__":
    main()
