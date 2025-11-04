class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        sum_s = 0
        sum_t = 0

        for val in s:
            sum_s += ord(val)
        
        for val in t:
            sum_t += ord(val)

        diff = sum_t - sum_s

        return chr(diff)