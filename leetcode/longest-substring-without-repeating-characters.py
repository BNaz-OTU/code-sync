class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCount = 0
        let_set = set()
        left, right = 0, 0

        while right < len(s):
            if (s[right] in let_set):
                let_set.remove(s[left])
                left += 1
            else:
                let_set.add(s[right])
                right += 1
            
            maxCount = max(maxCount, len(let_set))
        
        return maxCount