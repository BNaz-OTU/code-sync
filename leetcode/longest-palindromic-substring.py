class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        word = ""

        for idx in range(len(s)):
            left, right = idx, idx
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (maxLen < (right - left + 1)):
                    maxLen = right - left + 1
                    word = s[left:right + 1]
                
                left -= 1
                right += 1
            
            left, right = idx, idx + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (maxLen < (right - left + 1)):
                    maxLen = right - left + 1
                    word = s[left:right + 1]
                
                left -= 1
                right += 1
        
        return word