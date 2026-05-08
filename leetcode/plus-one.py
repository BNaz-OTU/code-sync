class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_og = ""
        final = []

        for digit in digits:
            str_og += str(digit)
        
        str_mod = str(int(str_og) + 1)

        for n_digit in str_mod:
            final.append(int(n_digit))
        
        return final