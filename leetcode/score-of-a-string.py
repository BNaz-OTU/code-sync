class Solution:
    def scoreOfString(self, s: str) -> int:
        sumVal = 0
        for idx in range(1, len(s)):
            sumVal += abs(ord(s[idx]) - ord(s[idx - 1]))
            # print(val, ord(val))
        
        return sumVal