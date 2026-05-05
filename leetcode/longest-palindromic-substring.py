class Solution:
    def longestPalindrome(self, s: str) -> str:
        final = ""
        maxLen = 0

        for idx in range(len(s)):
            # ODD CASE
            left = idx
            right = idx

            while left >= 0 and right < len(s) and s[right] == s[left]:
                if (maxLen < (right - left + 1)):
                    final = s[left:right + 1]
                    maxLen = (right - left + 1)

                left -= 1
                right += 1
            
            # EVEN CASE
            left = idx
            right = idx + 1
            while left >= 0 and right < len(s) and s[right] == s[left]:
                if (maxLen < (right - left + 1)):
                    final = s[left:right + 1]
                    maxLen = right - left + 1
                
                left -= 1
                right += 1
        
        return final