class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]

        for idx in range(1, len(prices)):
            sell = prices[idx]

            if (sell < buy):
                buy = sell
            
            max_profit = max(max_profit, sell - buy)
        
        return max_profit