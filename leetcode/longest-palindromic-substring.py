class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Credit (NeetCode): https://www.youtube.com/watch?v=XYQecbcd6_c

        res = ""
        resLen = 0

        for idx in range(len(s)):
            # Odd Check
            left = idx
            right = idx

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if ((right - left + 1) > resLen):
                    res = s[left:right + 1]
                    resLen = right - left + 1
                
                left -= 1
                right += 1

            # Even Check
            left = idx
            right = idx + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if ((right - left + 1) > resLen):
                    res = s[left: right + 1]
                    resLen = right - left + 1
                
                left -= 1
                right += 1      


        return res