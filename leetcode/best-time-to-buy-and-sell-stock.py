class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for price in prices[1:]:
            sell = price

            if (sell - buy < 0):
                buy = sell
            
            profit = max(profit, sell - buy)
        
        return profit