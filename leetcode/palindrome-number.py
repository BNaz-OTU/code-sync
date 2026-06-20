class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        middle = len(str_x) // 2

        if (len(str_x) % 2 == 1):
            left, right = middle, middle

            while str_x[left] == str_x[right]:
                left -= 1
                right += 1

                if (left < 0):
                    return True
            
            return False
        
        else:
            left, right = middle - 1, middle

            while str_x[left] == str_x[right]:
                left -= 1
                right += 1

                if (left < 0):
                    return True
            
            return False