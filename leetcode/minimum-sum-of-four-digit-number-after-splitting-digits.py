class Solution:
    def minimumSum(self, num: int) -> int:
        
        str_num = str(num)
        digits = []
        new1 = []
        new2 = []

        for val in str_num:
            digits.append(val)

        # Sort the list in descending order
        digits.sort(reverse=True)

        print(digits)

        new1 = digits.pop()
        new2 = digits.pop()
        new1 += digits.pop()
        new2 += digits.pop()

        return int(new1) + int(new2)