class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # Credit: https://www.youtube.com/watch?v=Q2Tw6gcVEwc
        
        if (numRows == 1):
            return s
        
        res = ""
        for row in range(numRows):
            increment = 2 * (numRows - 1)

            for idx in range(row, len(s), increment):
                res += s[idx]

                if (row > 0 and row < numRows - 1 and idx + increment - 2 * row < len(s)):
                    res += s[idx + increment - 2 * row]
        
        return res