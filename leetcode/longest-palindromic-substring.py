class Solution:
    def longestPalindrome(self, s: str) -> str:
        finalStr = ""
        longest = 0

        for idx in range(len(s)):
            # ODD CASE
            left = idx
            right = idx
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if ((right - left + 1) > longest):
                    longest = (right - left + 1)
                    finalStr = s[left : right + 1]
                
                left -= 1
                right += 1
            
            # EVEN CASE
            left = idx
            right = idx + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if ((right - left + 1) > longest):
                    longest = (right - left + 1)
                    finalStr = s[left : right + 1]
                
                left -= 1
                right += 1

        return finalStr