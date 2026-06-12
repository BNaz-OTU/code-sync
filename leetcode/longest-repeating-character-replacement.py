class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        left = 0
        maxLen = 0

        for right in range(len(s)):
            if (s[right] not in hashMap):
                hashMap[s[right]] = 0
            
            hashMap[s[right]] += 1

            while (right - left + 1) - max(hashMap.values()) > k:
                hashMap[s[left]] -= 1
                left += 1
            
            maxLen = max(maxLen, right - left + 1)

        return maxLen