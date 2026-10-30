class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        visit = set()

        for right in range(len(s)):
            while s[right] in visit:
                visit.remove(s[left])
                left += 1
            
            longest = max(longest, right - left + 1)
            visit.add(s[right])
        
        return longest