# -*- coding: utf-8 -*-

class PrettyName():
    def prettyName(self, name: 'str') -> 'int':
        table = {}
        for char in name:
            if char.lower() not in table:
                table[char.lower()] = 1
            else:
                table[char.lower()] += 1
        sorted_appearance = sorted(table.values(), reverse=True)
        ans = 0
        for i in range(len(sorted_appearance)):
            ans += (26 - i) * sorted_appearance[i]
        return ans

def main():
    test = PrettyName()
    print(test.prettyName("zhangsan"))
    print(test.prettyName("lisi"))

if __name__ == "__main__":
    main()