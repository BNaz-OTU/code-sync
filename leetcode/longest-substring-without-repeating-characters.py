class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow = 0
        fast = 0
        maxLen = 0
        set_let = set()

        while fast < len(s):
            while s[fast] in set_let:
                set_let.remove(s[slow])
                slow += 1
            
            set_let.add(s[fast])
            maxLen = max(len(set_let), maxLen)
            fast += 1
        
        return maxLen