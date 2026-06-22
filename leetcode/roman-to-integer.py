class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        total = 0
        for idx in range(len(s) - 1):
            if (roman[s[idx]] < roman[s[idx + 1]]):
                total -= roman[s[idx]]
            
            else:
                total += roman[s[idx]]
        
        total += roman[s[-1]]
        return total