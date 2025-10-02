class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dictPattern = {}
        dictWord = {}
        s_list = s.split(" ")

        if (len(pattern) != len(s_list)):
            return False
        

        for idx in range(len(pattern)):
            if (s_list[idx] in dictWord and dictWord[s_list[idx]] != pattern[idx]):
                return False
            else:
                dictWord[s_list[idx]] = pattern[idx]

            if (pattern[idx] in dictPattern and dictPattern[pattern[idx]] != s_list[idx]):
                return False
            else:
                dictPattern[pattern[idx]] = s_list[idx]
        
        return True
                
                

        return True