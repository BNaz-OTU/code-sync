class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        letSet = set()
        # letSet.add(s[left])
        maxCount = 0

        for right in range(len(s)):
            while (s[right] in letSet):
                letSet.remove(s[left])
                left += 1
            
            else:
                letSet.add(s[right])
            
            maxCount = max(maxCount, len(letSet))
        
        return maxCount