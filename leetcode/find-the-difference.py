class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        # Numerical/ASCII Method
        # Credit NeetCode: https://www.youtube.com/watch?v=oFmv4N4z00c

        sum_s = 0
        sum_t = 0

        for val in s:
            sum_s += ord(val)
        
        for val in t:
            sum_t += ord(val)
        
        return chr(abs(sum_s - sum_t))