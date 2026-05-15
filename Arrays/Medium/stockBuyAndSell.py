class Solution:
    def maxProfit(self, prices):
        profit = 0
        i  = 0

        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]: #if the price of the stock next day is greater, we can buy the stock today and sell it next dayand add the difeerence in profit
                profit+=(prices[i+1]-prices[i])
        return profit
    
a = Solution()
print(a.maxProfit([100, 180, 260, 310, 40, 535, 695]))