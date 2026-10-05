class Solution:
    def reverse(self, x: int) -> int:
        isNegative = False

        if (x < 0):
            isNegative = True
            x *= -1
        
        new_x = str(x)[::-1]

        if (isNegative):
            new_x = "-" + new_x
        
        new_x = int(new_x)

        if (new_x < (-2 ** 31) or new_x > (2 ** 31) - 1):
            return 0
        
        return new_x