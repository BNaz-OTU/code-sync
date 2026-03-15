class Solution:
    def longestPalindrome(self, s: str) -> str:
        # USED SOLN: https://www.youtube.com/watch?v=XYQecbcd6_c
        if (len(s) == 1):
            return s

        maxCount = 0
        pali = ""

        for idx in range(len(s) - 1):
            left = idx
            right = idx
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if ((right - left + 1) > maxCount):
                    pali = s[left:right + 1]
                    maxCount = right - left + 1
                left -= 1
                right += 1
            
            left = idx
            right = idx + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if ((right - left + 1) > maxCount):
                    pali = s[left:right + 1]
                    maxCount = right - left + 1
                left -= 1
                right += 1

        return pali