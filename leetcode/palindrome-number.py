class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        
        divisor = 1

        while divisor * 10 < x:
            divisor *= 10
        
        while x:
            front = x // divisor
            end = x % 10

            if (front != end):
                return False
            
            x1 = x % divisor
            x2 = x1 // 10
            x = x2
            divisor = divisor // 100
        
        return True