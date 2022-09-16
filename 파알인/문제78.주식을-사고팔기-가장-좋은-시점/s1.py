# 122. Best Time to Buy and Sell Stock II
# 220916

class Solution(object):
    def maxProfit(self, prices):
        
        sell = buy = 0
        sell_i = buy_i = 0
        profit = 0
        for i in range(len(prices)):
            # i가 0이 아닐 때 전날과 비교
            if i: 
                # 값이 떨어지면 buy 갱신하고 팔기
                if prices[i-1] > prices[i]:
                    if buy_i < sell_i:
                        profit += sell - buy
                    buy = prices[i]
                    buy_i = i
                # 값이 오르면 sell 갱신
                elif prices[i-1] < prices[i]:
                    sell = prices[i]
                    sell_i = i
            else:
                buy = sell = prices[i]
                buy_i = sell_i = i
        else:
            if buy_i < sell_i:
                        profit += sell - buy
        return profit

prices = [7,1,5,3,6,4]
# prices = [1,2,3,4,5]
# prices = [2,1,2,0,1]
s = Solution()
print(s.maxProfit(prices))