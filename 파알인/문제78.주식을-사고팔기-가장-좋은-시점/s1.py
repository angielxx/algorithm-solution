# 122. Best Time to Buy and Sell Stock II
# 220916

# 좀 더럽게 푼듯..

class Solution(object):
    def maxProfit(self, prices):
        
        # 사는 가격, 파는 가격
        sell = buy = 0
        # 사는 시점, 파는 시점
        sell_i = buy_i = 0

        profit = 0
        for i in range(len(prices)):
            # i가 0이 아닐 때 전날과 비교
            if i: 
                # 값이 떨어지면 사야하는 날이므로 buy 갱신하고 팔기
                if prices[i-1] > prices[i]:

                    # 마지막에 값이 떨어지고 sell이 갱신되지 않은 경우 방지
                    # 산 날이 판 날 보다 과거일 때만 판다.
                    if buy_i < sell_i:
                        profit += sell - buy

                    # 계속 떨어지는 경우 profit계산되지 않고 buy만 계속 갱신됨
                    buy = prices[i]
                    buy_i = i

                # 값이 오르면 sell 갱신
                # 계속 오르면 계속 갱신하게 된다.
                elif prices[i-1] < prices[i]:
                    sell = prices[i]
                    sell_i = i

            # i가 0이면 첫째날의 가격으로 모두 갱신
            else:
                buy = sell = prices[i]
                buy_i = sell_i = i
                
        # 마지막 날에 오르고 끝난 경우 계산이 안 되는 예외 처리
        else:
            if buy_i < sell_i:
                        profit += sell - buy
        return profit

prices = [7,1,5,3,6,4]
# prices = [1,2,3,4,5]
# prices = [2,1,2,0,1]
s = Solution()
print(s.maxProfit(prices))