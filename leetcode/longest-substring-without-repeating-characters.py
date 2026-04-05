class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visit = set()
        left = 0
        maxCount = 0

        for right in range(len(s)):
            while s[right] in visit:
                visit.remove(s[left])
                left += 1
            
            visit.add(s[right])
            maxCount = max(maxCount, len(visit))

        return maxCount