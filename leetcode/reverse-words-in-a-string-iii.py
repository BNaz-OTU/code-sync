class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(" ")

        for idx in range(len(s_list)):
            word = s_list[idx]
            left = 0
            right = len(word) - 1
            iter_word = list(word)

            while left < right:
                iter_word[left], iter_word[right] = iter_word[right], iter_word[left]
                left += 1
                right -= 1
            print(iter_word)
            s_list[idx] = "".join(iter_word)
        
        return " ".join(s_list)