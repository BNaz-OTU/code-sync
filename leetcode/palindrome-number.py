class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        
        div = 1

        while div * 10 <= x:
            div *= 10
        
        # print(x // div)
        while x > 0:
            front = x // div
            back = x % 10
            print(front, back)
            if (front != back):
                return False
            
            x1 = x % div
            x2 = x1 // 10
            div = div // 100

            x = x2
        
        return True