class Solution:
    def reverseWords(self, s: str) -> str:
        sentenceWords = s.split(" ")

        for idx in range(len(sentenceWords)):
            word = list(sentenceWords[idx])
            left = 0
            right = len(word) - 1

            while (left < right):
                word[left], word[right] = word[right], word[left]
                left += 1
                right -= 1
            
            sentenceWords[idx] = "".join(word)
        
        return " ".join(sentenceWords)