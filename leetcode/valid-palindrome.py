class Solution:
    def isPalindrome(self, s: str) -> bool:
        pali_temp = ""

        for letter in s.lower():
            if (letter.isalnum()):
                pali_temp += letter

        left = 0
        right = len(pali_temp) - 1

        while left < right:
            # print(f'Left: {left} | Right: {right}')
            if (pali_temp[left] == pali_temp[right]):
                left += 1
                right -= 1
            else:
                return False
            
        return True