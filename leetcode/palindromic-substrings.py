class Solution:
    def countSubstrings(self, s: str) -> int:
        paliCount = 0

        def checker(left, right):
            nonlocal paliCount
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                paliCount += 1
                left -= 1
                right += 1

        for idx in range(len(s)):
            # ODD CASE
            checker(idx, idx)

            # EVEN CASE
            checker(idx, idx + 1)

        return paliCount