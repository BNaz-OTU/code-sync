class Solution:
    def longestPalindrome(self, s: str) -> str:
        final = ""
        idx = 0

        while idx < len(s):
            left = idx
            right = idx

            while left >= 0 and right < len(s) and s[left] == s[right]:
                counter = right - left + 1

                if (counter > len(final)):
                    final = s[left : right + 1]
                
                left -= 1
                right += 1
            
            left = idx
            right = idx + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                counter = right - left + 1
                
                if (counter > len(final)):
                    final = s[left : right + 1]
                
                left -= 1
                right += 1

            idx += 1

        return final