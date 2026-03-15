class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for idx in range(len(s)):
            # Odd Case
            left = idx
            right = idx
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            
            # Even Case
            left = idx 
            right = idx + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            
        return count