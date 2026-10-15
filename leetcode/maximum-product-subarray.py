class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_num = max(nums)

        dp = [1, 1]

        for n in nums:
            if n == 0:
                dp = [1, 1]
                continue
            
            tmp = dp[0] * n
            dp[0] = max(n * dp[0], n * dp[1], n)
            dp[1] = min(tmp, n * dp[1], n)
            max_num = max(max_num, dp[0])
        
        return max_num