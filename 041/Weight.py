# -*- coding: utf-8 -*-

class Weight():
    def weight(self, w: 'list[int]', n: 'list[int]') -> 'list[int]':

        ans = [0, ]
        for i in range(len(w)):
            temp = ans[:]
            for j in range(1, n[i] + 1):
                for elem in temp:
                    ans.append(elem + w[i] * j)
                ans = list(set(ans))
        return ans

def main():
    test = Weight()
    print(test.weight([1, 2], [2, 1]))

if __name__ == "__main__":
    main()