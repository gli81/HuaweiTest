# -*- coding: utf-8 -*-

class ShoppingList:
    def shoppingList(self, weight: 'list[int]', value: 'list[int]', subs: 'list[int]', balance: 'int') -> 'int':
        ct = len(weight)
        ## deal with 10 folds
        balance = int(balance / 10)
        for num in weight:
            num = int(num / 10)
        ## build a modified 2D array
        w_list = [[0 for i in range(3)] for i in range(ct)]
        v_list = [[0 for i in range(3)] for i in range(ct)]
        for i in range(ct):
            if subs[i] == 0: ## not sub
                w_list[i][0] = int(weight[i] / 10)
                v_list[i][0] = value[i]
            else:
                if w_list[subs[i] - 1][1] == 0: ## first subsidiary
                    w_list[subs[i] - 1][1] = int(weight[i] / 10)
                    v_list[subs[i] - 1][1] = value[i]
                else: ## second subsidiary
                    w_list[subs[i] - 1][2] = int(weight[i] / 10)
                    v_list[subs[i] - 1][2] = value[i]
        for item in w_list:
            try:
                w_list.remove([0, 0, 0])
            except:
                pass
        for item in v_list:
            try:
                v_list.remove([0, 0, 0])
            except:
                pass
        # print(w_list)
        # print(v_list)
        ## dp
        non_sub_ct = len(w_list)
        dp = [[0 for i in range(balance)] for j in range(non_sub_ct)]
        for j in range(balance):
            if j >= sum(w_list[0]): ## all
                dp[0][j] = sum(v_list[0])
            elif j >= w_list[0][0] + w_list[0][1]: ## nonsub & first sub
                dp[0][j] = v_list[0][0] + v_list[0][1]
            elif j >= w_list[0][0] + w_list[0][2]: ## nonsub & second sub
                dp[0][j] = v_list[0][0] + v_list[0][2]
            elif j >= w_list[0][0]: ## nonsub only
                dp[0][j] = v_list[0][0]
        ans = -1
        for j in range(1, len(dp[0])):
            for i in range(1, len(dp)):
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w_list[i][0]] + v_list[i][0],\
                    dp[i - 1][j - w_list[i][0] - w_list[i][1]] + v_list[i][0] + v_list[i][1],\
                        dp[i - 1][j - w_list[i][0] - w_list[i][2]] + v_list[i][0] + v_list[i][2],\
                            dp[i - 1][j - w_list[i][0] - w_list[i][1] - w_list[i][2]] + v_list[i][0] + v_list[i][1] + v_list[i][2])
                if dp[i][j] > ans:
                    ans = dp[i][j]
        for i in dp:
            print(i)
        return ans

    
    def zeroOneBag(self, weight: 'list[int]', value:'list[int]', balance: 'int') -> 'int':
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
    print(test.shoppingList([20, 20, 10, 10, 10], [3, 3, 3, 2, 1], [5, 5, 0, 0, 0], 50))
    print(test.shoppingList([800, 400, 300, 400, 500], [2, 5, 5, 3, 2], [0, 1, 1, 0, 0], 1000))
    # print(test.zeroOneBag([800, 400, 300, 400, 500], [2, 5, 5, 3, 2], 1000))

if __name__ == '__main__':
    main()
