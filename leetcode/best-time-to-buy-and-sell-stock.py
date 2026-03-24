class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = None
        sell = None

        for price in prices:
            if (buy is None):
                buy = price
                continue
            sell = price
            # print(f"Price: {price} | Buy: {buy} | Sell: {sell}")
            
            profit = sell - buy

            if (profit <= 0):
                buy = sell
                continue
            
            maxProfit = max(maxProfit, profit)
        
        return maxProfit