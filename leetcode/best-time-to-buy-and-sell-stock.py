class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        fast = 0
        slow = 0

        while fast < len(prices):
            if (prices[slow] > prices[fast]):
                slow = fast
            
            elif (prices[slow] < prices[fast]):
                maxProfit = max(maxProfit, prices[fast] - prices[slow])

            fast += 1
        
        return maxProfit