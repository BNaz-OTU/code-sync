class Solution:
    def maximum69Number (self, num: int) -> int:
        # Better way to solve the problem: https://www.youtube.com/shorts/9aRMN8IZdP0
        
        str_69 = []
        found = False
        final = ""
        for num in str(num):
            str_69.append(num)

        print(str_69)

        for idx, val in enumerate(str_69):
            if (val == "6" and found == False):
                final += "9"
                found = True
            else:
                final += val
        
        return int(final)