class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(" ")

        for idx in range(len(s_list)):
            word = s_list[idx]
            left = 0
            right = len(word) - 1
            split_word = list(word)

            while left < right:
                split_word[left], split_word[right] = split_word[right], split_word[left]
                left += 1
                right -= 1
            print(split_word)
            
            s_list[idx] = "".join(split_word)
        
        return " ".join(s_list)