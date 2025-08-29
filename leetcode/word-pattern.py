class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict_word_to_let = {}
        dict_let_to_word = {}
        new_s = s.split(" ")

        if (len(new_s) != len(pattern)):
            return False

        for idx in range(len(pattern)):
            if (new_s[idx] in dict_word_to_let and dict_word_to_let[new_s[idx]] != pattern[idx]):
                return False

            if (pattern[idx] in dict_let_to_word and dict_let_to_word[pattern[idx]] != new_s[idx]):
                return False
            
            dict_word_to_let[new_s[idx]] = pattern[idx]
            dict_let_to_word[pattern[idx]] = new_s[idx]
        
        return True