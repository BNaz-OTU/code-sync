class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict_pattern = {}
        dict_s = {}
        new_s = s.split(" ")

        if (len(pattern) != len(new_s)):
            return False

        for idx in range(len(pattern)):
            if (pattern[idx] not in dict_pattern):
                dict_pattern[pattern[idx]] = new_s[idx]
            elif (pattern[idx] in dict_pattern and dict_pattern[pattern[idx]] == new_s[idx]):
                continue
            else:
                return False
        
        for idx in range(len(pattern)):
            if (new_s[idx] not in dict_s):
                dict_s[new_s[idx]] = pattern[idx]
            elif (new_s[idx] in dict_s and dict_s[new_s[idx]] == pattern[idx]):
                continue
            else:
                return False
        
        return True
        # print(new_s)