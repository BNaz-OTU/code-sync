class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
            
        is_negative = True if x < 0 else False

        if (is_negative):
            x = x * -1

        new_x = ""

        while x > 0:
            last = x % 10
            new_x += str(last)
            x = x // 10
        
        num = int(new_x)

        if (is_negative):
            num *= - 1
        
        if (-2**31 <= num <= 2**31):
            return num
        
        return 0