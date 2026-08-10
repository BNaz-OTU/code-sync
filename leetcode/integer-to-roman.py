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

        for nRom, cRom in roman:
            if (num // nRom == 0):
                continue
            else:
                val = num // nRom
                final += val * cRom
                num = num % nRom
        
        return final