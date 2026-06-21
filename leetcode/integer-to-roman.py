class Solution:
    def intToRoman(self, num: int) -> str:
        roman = [
            [1000, "M"],
            [900, "CM"],
            [500, "D"],
            [400, "CD"],
            [100, "C"],
            [90, "XC"],
            [50, "L"],
            [40, "XL"],
            [10, "X"],
            [9, "IX"],
            [5, "V"],
            [4, "IV"],
            [1, "I"]
        ]

        final = ""

        for value, sym in roman:
            count = num // value

            if (count > 0):
                final += (count * sym)
            
            num = num % value
        
        return final