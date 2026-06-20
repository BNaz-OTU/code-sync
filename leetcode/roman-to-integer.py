class Solution:
    def romanToInt(self, s: str) -> int:
        sumVal = 0
        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        for idx in range(len(s) - 1):
            cur = roman[s[idx]]
            nxt = roman[s[idx + 1]]

            if (cur < nxt):
                sumVal -= cur
            
            else:
                sumVal += cur
            
        sumVal += roman[s[-1]]
        
        return sumVal