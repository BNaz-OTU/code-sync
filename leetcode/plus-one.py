class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_temp = ""
        final = []

        for digit in digits:
            str_temp += str(digit)
        
        n_str = str(int(str_temp) + 1)

        for n_digit in n_str:
            final.append(int(n_digit))
        
        return final