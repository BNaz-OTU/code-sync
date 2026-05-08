class Solution:
    def longestPalindrome(self, s: str) -> str:
        long_str = ""
        maxLen = 0

        for idx in range(len(s)):
            left = idx
            right = idx

            while right < len(s) and left >= 0 and s[right] == s[left]:
                if (maxLen < (right - left + 1)):
                    long_str = s[left: right + 1]
                    maxLen = right - left + 1
                
                left -= 1
                right += 1
            
            left = idx
            right = idx + 1
            while right < len(s) and left >= 0 and s[right] == s[left]:
                if (maxLen < (right - left + 1)):
                    long_str = s[left: right + 1]
                    maxLen = right - left + 1
                
                left -= 1
                right += 1
        
        return long_str