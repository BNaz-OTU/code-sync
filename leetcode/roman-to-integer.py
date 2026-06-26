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
            cur = s[idx]
            nxt = s[idx + 1]
            if (roman[cur] < roman[nxt]):
                total -= roman[cur]
            
            else:
                total += roman[cur]
        
        total += roman[s[-1]]

        return total