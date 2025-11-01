class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        list_s = list(s)

        left = 0
        right = len(s) - 1

        while left < right:
            if (list_s[left] in vowels and list_s[right] in vowels):
                list_s[left], list_s[right] = list_s[right], list_s[left]
                left += 1
                right -= 1
            
            if (list_s[left] not in vowels):
                left += 1
            
            if (list_s[right] not in vowels):
                right -= 1
        
        return "".join(list_s)