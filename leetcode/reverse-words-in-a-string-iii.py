class Solution:
    def reverseWords(self, s: str) -> str:
        split_words = s.split(" ")
        
        for idx in range(len(split_words)):
            left = 0
            right = len(split_words[idx]) - 1
            list_word = list(split_words[idx])

            while left < right:
                list_word[left], list_word[right] = list_word[right], list_word[left]
                left += 1
                right -= 1
            
            split_words[idx] = "".join(list_word)
        
        return " ".join(split_words)