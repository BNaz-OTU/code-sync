class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        
        # dp = 0
        for idx in range(len(cost) - 3, -1, -1):
            cost[idx] = cost[idx] + min(cost[idx + 1], cost[idx + 2])
        
        return min(cost[0], cost[1])