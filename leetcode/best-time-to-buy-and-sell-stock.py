class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxProfit = 0

        for price in prices:
            sell = price

            if (sell - buy < 0):
                buy = sell
                continue
            
            maxProfit = max(maxProfit, sell - buy)
        
        return maxProfit