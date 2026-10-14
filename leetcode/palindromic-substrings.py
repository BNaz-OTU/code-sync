class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def paliChecker(idx, count):
            # Check Even
            left, right = idx, idx + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            
            # Check Odd
            left, right = idx - 1, idx + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            
            return count

        
        for idx in range(len(s)):
            count += 1
            count += paliChecker(idx, 0)
        
        return count