# -*- coding: utf-8 -*-

class ShoppingList:
    def shoppingList(self, weight: 'list[int]', value: 'list[int]', subs: 'list[int]', balance: 'int', count: 'int') -> 'int':
        pass
    
    def zeroOneBag(self, weight: 'list[int]', value:'list[int]', balance: 'int', count:'int') -> 'int':
        dp = [[0 for i in range(int(balance / 10))] for i in range(len(weight))]
        for j in range(len(dp[0])):
            if j >= weight[0] / 10:
                dp[0][j] = value[0]
        ans = 0
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - int(weight[i]/10)] + value[i])
                if dp[i][j] > ans:
                    ans = dp[i][j]
        return ans

def main():
    test = ShoppingList()
    print(test.shoppingList([800, 400, 300, 400, 500], [2, 5, 5, 3, 2], [0, 1, 1, 0, 0], 1000, 5))
    print(test.zeroOneBag([800, 400, 300, 400, 500], [2, 5, 5, 3, 2], 1000, 5))

if __name__ == '__main__':
    main()
