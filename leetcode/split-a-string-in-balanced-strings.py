class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l_count, r_count, count = 0, 0, 0

        for val in s:
            if (val == "R"):
                r_count += 1
            elif (val == "L"):
                l_count += 1
            
            if (r_count == l_count):
                count += 1
                l_count, r_count = 0, 0
        
        return count