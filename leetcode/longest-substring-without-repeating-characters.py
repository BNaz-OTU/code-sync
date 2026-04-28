class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxLen = 0

        if (len(s) == 0):
            return maxLen
        right = 0

        for left in range(len(s)):
            Val = s[left]
            while Val in seen:
                seen.remove(s[right])
                right += 1
            
            seen.add(Val)
            maxLen = max(maxLen, (left - right) + 1)
        
        return maxLen