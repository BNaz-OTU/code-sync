class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxProfit = 0
        buy = prices[0]

        for sell in prices:
            if (sell > buy):
                maxProfit = max(maxProfit, sell - buy)
            else:
                buy = sell
        
        return maxProfit