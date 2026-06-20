class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)

        left, right = 0, len(str_x) - 1

        while left < right and str_x[left] == str_x[right]:
            left += 1
            right -= 1

        if (left >= right):
            return True
        else:
            return False