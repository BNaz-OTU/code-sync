class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        digitCounter = 1

        while digitCounter * 10 <= x:
            digitCounter *= 10
                
        while digitCounter > 0:
            front = x // digitCounter
            back = x % 10

            if (front != back):
                return False
            
            x1 = x % digitCounter
            x2 = x1 // 10
            x = x2

            digitCounter = digitCounter // 100
        
        return True