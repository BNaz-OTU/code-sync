class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        
        div = 1

        while div * 10 <= x:
            div *= 10
        
        while x > 0:
            front = x // div
            back = x % 10

            if (front != back):
                return False

            # Remove number from front
            x1 = x % div

            # Remove number from back
            x2 = x1 // 10

            # Update 'x'
            x = x2

            # Update div
            div = div // 100
            

        return True