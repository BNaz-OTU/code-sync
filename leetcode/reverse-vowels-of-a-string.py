class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = 'aeiouAEIOU'

        left = 0
        right = len(s) - 1
        list_s = list(s)

        while left < right:
            if (list_s[left] in vowel and list_s[right] in vowel):
                list_s[left], list_s[right] = list_s[right], list_s[left]
                left += 1
                right -= 1

            elif (list_s[left] not in vowel and list_s[right] in vowel):
                left += 1
                
            elif (list_s[left] in vowel and list_s[right] not in vowel):
                right -= 1
            
            else:
                left += 1
                right -= 1
        
        final = ""

        for val in list_s:
            final += val
        
        return final