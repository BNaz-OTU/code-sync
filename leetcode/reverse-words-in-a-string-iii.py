class Solution:
    def reverseWords(self, s: str) -> str:
        # ** DIDNT USE SOLN, JUST CHECKING FOR REFERENCE: https://youtu.be/7kUEwiwwnlA?si=x6V2GyeHojULGdZR **
        s_list = s.split(" ")
        
        for idx in range(len(s_list)):
            char_list = list(s_list[idx])
            left = 0
            right = len(char_list) - 1

            while (left < right):
                char_list[left], char_list[right] = char_list[right], char_list[left]
                left += 1
                right -= 1
            
            s_list[idx] = "".join(char_list)
        
        return " ".join(s_list)