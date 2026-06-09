class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxLen = 0
        left = 0
        right = 0

        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            maxLen = max(maxLen, right - left + 1)
            right += 1
        
        return maxLen