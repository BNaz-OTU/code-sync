class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        visit = set()
        longest = 0

        for right in range(len(s)):

            while left < right and s[right] in visit:
                visit.remove(s[left])
                left += 1
            
            visit.add(s[right])
            longest = max(longest, right - left + 1)
        
        return longest