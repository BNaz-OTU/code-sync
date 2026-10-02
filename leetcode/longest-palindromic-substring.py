class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxSize = 0
        currPali = ""

        for idx in range(len(s)):
            left = idx
            right = idx
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > maxSize:
                    currPali = s[left: right + 1]
                    maxSize = right - left + 1
                
                left -= 1
                right += 1
            
            left = idx
            right = idx + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > maxSize:
                    currPali = s[left: right + 1]
                    maxSize = right - left + 1
                
                left -= 1
                right += 1
        
        return currPali