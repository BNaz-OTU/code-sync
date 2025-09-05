class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        maxCount = 0
        let_set = set()
        left, right = 0, 0

        while right < len(s):
            if (s[right] in let_set):
                let_set.remove(s[left])
                left += 1
                count -= 1
            else:
                let_set.add(s[right])
                count += 1
                right += 1
            
            maxCount = max(maxCount, count)
        
        return maxCount