class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashLet = {}
        count = 0
        left = 0

        for right in range(len(s)):
            if (s[right] in hashLet):
                hashLet[s[right]] += 1
            else:
                hashLet[s[right]] = 1
                
            while (right - left + 1) - max(hashLet.values()) > k:
                hashLet[s[left]] -= 1
                left += 1
            
            count = max(count, right - left + 1)
        
        return count