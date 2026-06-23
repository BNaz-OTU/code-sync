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
            
            # Remove front number
            x1 = x % div

            # Remove back number
            x2 = x1 // 10

            # Final updated number
            x = x2

            # Decrement div
            div = div / 100

        return True