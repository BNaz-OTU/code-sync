class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            if (s[right] not in hashmap):
                hashmap[s[right]] = 0
            
            hashmap[s[right]] += 1
            # print(hashmap)
            # print(right - left + 1 - max(hashmap.values()), ">", k)
            while ((right - left + 1) - max(hashmap.values())) > k:
                print("Hi")
                hashmap[s[left]] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)
        
        return longest