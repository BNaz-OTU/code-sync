class Solution:
    def countSubstrings(self, s: str) -> int:
        paliCount = 0

        for idx in range(len(s)):
            # ODD CASE
            left = idx
            right = idx

            while left >= 0 and right < len(s) and s[left] == s[right]:
                paliCount += 1
                left -= 1
                right += 1

            # EVEN CASE
            left = idx
            right = idx + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                paliCount += 1
                left -= 1
                right += 1
        
        return paliCount