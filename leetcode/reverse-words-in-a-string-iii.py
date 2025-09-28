class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(" ")

        for idx in range(len(s_list)):
            word = s_list[idx]
            split_word = list(word)
            left = 0 
            right = len(split_word) - 1

            # print(f"W: {word} | L: {word[left]} | R: {word[right]}")
            while left < right:
                split_word[left], split_word[right] = split_word[right], split_word[left]
                left += 1
                right -= 1

            s_list[idx] = "".join(split_word)
                    
        return " ".join(s_list)