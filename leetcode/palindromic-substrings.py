class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for idx in range(len(s)):
            # ODD Case
            left, right = idx, idx
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            # EVEN Case
            left, right = idx, idx + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        return count