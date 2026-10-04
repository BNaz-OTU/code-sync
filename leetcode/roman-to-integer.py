class Solution:
    def romanToInt(self, s: str) -> int:
        romanInt = {
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
            curr_numeral = s[idx]
            next_numeral = s[idx + 1]

            if (romanInt[curr_numeral] >= romanInt[next_numeral]):
                total += romanInt[curr_numeral]
            
            else:
                total -= romanInt[curr_numeral]
        
        total += romanInt[s[-1]]

        return total