class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        
        divisor = 1

        while (divisor * 10) < x:
            divisor *= 10
        
        while x > 0:
            front = x // divisor
            back = x % 10

            if (front != back):
                return False
            
            x1 = x % divisor
            x2 = x1 // 10
            x = x2
            divisor = divisor // 100
        
        return True