class Solution:
    def longestPalindrome(self, s: str) -> str:
        finalS = ""
        longest = 0

        def checker(left, right):
            nonlocal longest, finalS

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (longest < (right - left + 1)):
                    longest = (right - left + 1)
                    finalS = s[left : right + 1]

                left -= 1
                right += 1

        for idx in range(len(s)):
            # ODD CASE
            checker(idx, idx)

            # EVEN CASE
            checker(idx, idx + 1)
        
        return finalS