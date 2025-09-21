class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"

        s_list = list(s)

        left = 0
        right = len(s) - 1

        while (left <= right):
            if (s_list[left] in vowels and s_list[right] in vowels):
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
                continue

            if (s_list[right] not in vowels):
                right -= 1
            
            if (s_list[left] not in vowels):
                left += 1
        
        return "".join(s_list)