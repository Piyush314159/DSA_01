class Solution1:
    def maxProfit(self, prices):
        profit = 0

        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]: #if the price of the stock next day is greater, we can buy the stock today and sell it next dayand add the difeerence in profit
                profit+=(prices[i+1]-prices[i])
        return profit
    
a = Solution1()
print(a.maxProfit([100, 180, 260, 310, 40, 535, 695]))


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        i = 0                         # buy day
        j = 1                         # sell day
        max_profit = 0

        while j < n:
            if prices[j] > prices[i]: # j is the sell day
                max_profit = max(max_profit, prices[j]-prices[i])
            else:                     # prices[j] < prices[i], j is the buy day
                i = j
            j += 1                    #                          
        
        return max_profit

class Solution2:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_prof = 0

        for price in prices:
            min_price = min(min_price, price)           # keep track of the minimum price so far
            max_prof = max(max_prof, price - min_price) # keep track of the maximum profit so far

        return max_prof