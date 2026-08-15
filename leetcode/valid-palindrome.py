class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            leftVal, rightVal = s[left], s[right]

            if (not leftVal.isalnum()):
                left += 1
                continue
            
            if (not rightVal.isalnum()):
                right -= 1
                continue
            
            if (leftVal.lower() != rightVal.lower()):
                return False
            
            left += 1
            right -= 1

        return True