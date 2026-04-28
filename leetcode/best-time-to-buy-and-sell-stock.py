class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        buy = prices[0]

        for sell in prices[1:]:
            if (sell - buy < 0):
                buy = sell
            else:
                maxProfit = max(maxProfit, sell - buy)
        
        return maxProfit