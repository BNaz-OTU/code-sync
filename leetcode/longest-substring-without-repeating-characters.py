class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # ** CHECKING SOLN ONLY FOR REF: https://www.youtube.com/watch?v=wiGpQwVHdE0 **

        maxCount = 0
        let_set = set()

        slow = 0
        fast = 0
        count = 0

        while fast < len(s):
            if (s[fast] in let_set):
                let_set.remove(s[slow])
                slow += 1
                count -= 1
            else:
                let_set.add(s[fast])
                fast += 1
                count += 1
                maxCount = max(maxCount, count)
        
        return maxCount