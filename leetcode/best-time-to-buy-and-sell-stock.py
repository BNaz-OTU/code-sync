class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxProfit = 0

        for sell in prices:
            if (sell < buy):
                # print(f"#1: Buy: {buy} | Sell: {sell} ")
                buy = sell
            
            else:
                # print(f"#2: Buy: {buy} | Sell: {sell} ")
                profit = sell - buy
                maxProfit = max(maxProfit, profit)
        
        return maxProfit