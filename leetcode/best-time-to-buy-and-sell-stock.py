class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for sell in prices[1:]:
            if sell < buy:
                buy = sell
                continue
            
            profit = max(profit, sell - buy)
        
        return profit