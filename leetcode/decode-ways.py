class Solution:
    def numDecodings(self, s: str) -> int:
        if (s[0] == "0"):
            return 0
        
        dp = [1, 1]

        for idx in range(len(s) - 1, -1, -1):
            if (s[idx] == "0"):
                cur = 0
            
            else:
                cur = dp[0]
                if ((idx + 1) < len(s) and (10 <= int(s[idx: idx + 2]) <= 26)):
                    cur += dp[1]
            
            dp[0], dp[1] = cur, dp[0]
        
        return dp[0]