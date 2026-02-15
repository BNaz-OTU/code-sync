class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zero_count = 0
        one_count = 0

        for val in s:
            if (val == "0"):
                zero_count += 1
            else:
                one_count += 1
        
        print(zero_count)
        print(one_count)

        if (one_count == 1):
            z_str = "0" * zero_count
            o_str = "1"
            return z_str + o_str
        
        z_str = "0" * zero_count
        o_str_1 = "1" * (one_count - 1)

        return o_str_1 + z_str + "1"