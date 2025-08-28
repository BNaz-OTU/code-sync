class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        maxProfit = 0

        for idx in range(1, len(prices)):
            sell = idx

            if (prices[buy] > prices[sell]):
                buy = sell
            else:
                maxProfit = max(maxProfit, prices[sell] - prices[buy])
        
        return maxProfit