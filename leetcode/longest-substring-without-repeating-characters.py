class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        let_set = set()

        left = 0
        right = 0
        maxCount = 0

        while right < len(s):
            if (s[right] in let_set):
                let_set.remove(s[left])
                left += 1
            else:
                let_set.add(s[right])
                right += 1

            maxCount = max(maxCount, right - left)
            
        
        return maxCount