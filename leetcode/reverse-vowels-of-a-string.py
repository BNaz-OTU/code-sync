class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Two Pointer Approach:
        First establish a variable containing all the vowels, which will later be used to check if 
        the character is a vowel. Setup a left and right pointer to traverse both sides of the string.
        In the event that a character on both pointers is a vowel swap the characters, then continue 
        incrementing the pointers to keep advancing thru the 'string'. Also, increment whenever a pointer 
        isn't a vowel.
        """

        vowel = "aeiouAEIOU"
        s_list = list(s)

        left = 0
        right = len(s) - 1

        while left < right:
            if (s_list[left] in vowel and s_list[right] in vowel):
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
            
            if (s_list[right] not in vowel):
                right -= 1
            
            if (s_list[left] not in vowel):
                left += 1
        
        return "".join(s_list)