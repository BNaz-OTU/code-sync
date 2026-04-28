class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        for val in set(s):
            hashMap[val] = 0
        right = 0
        maxVal = 0

        for left in range(len(s)):
            if (s[left] in hashMap):
                hashMap[s[left]] += 1
            
            val = ((left - right) + 1) - max(hashMap.values())

            while val > k:
                hashMap[s[right]] -= 1
                right += 1
                val = ((left - right) + 1) - max(hashMap.values())
            
            maxVal = max(maxVal, ((left - right) + 1))
        
        return maxVal