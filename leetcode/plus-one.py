class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_1 = ""

        for digit in digits:
            str_1 += str(digit)
        
        str_2 = str(int(str_1) + 1)

        final = []
        for new_digit in str_2:
            final.append(int(new_digit))
        
        return final