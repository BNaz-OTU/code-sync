class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        hashmap = {}
        maxLen = 0

        for right in range(len(s)):
            frontWord = s[right]

            if frontWord not in hashmap:
                hashmap[frontWord] = 0
            
            hashmap[frontWord] += 1

            while right - left - max(hashmap.values()) >= k:
                lastWord = s[left]
                hashmap[lastWord] -= 1
                left += 1
            
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen