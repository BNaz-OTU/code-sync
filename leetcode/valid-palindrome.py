class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left <= right:
            l_val = s[left]
            r_val = s[right]

            if (l_val.isalnum() == False):
                left += 1
                continue

            if (r_val.isalnum() == False):
                right -= 1
                continue
            
            if (l_val.lower() != r_val.lower()):
                return False
            
            left += 1
            right -= 1
            
        return True