class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 0]

        for _ in range(n):
            temp = dp[0]
            dp[0] = dp[0] + dp[1]
            dp[1] = temp
        
        return dp[0]