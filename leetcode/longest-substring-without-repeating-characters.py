class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visit = set()
        maxLen = 0

        left = 0
        for right in range(len(s)):
            while s[right] in visit:
                visit.remove(s[left])
                left += 1
            
            visit.add(s[right])
            maxLen = max(maxLen, right - left + 1)
            
        return maxLen