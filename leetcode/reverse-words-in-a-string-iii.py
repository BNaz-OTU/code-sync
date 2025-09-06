class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split(" ")

        for idx in range(len(word_list)):
            word = list(word_list[idx])
            left = 0
            right = len(word) - 1

            while (left < right):
                word[left], word[right] = word[right], word[left]
                left += 1
                right -= 1
            
            word_list[idx] = "".join(word)
        
        return " ".join(word_list)