class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        tMap = {}
        sMap = {}
        final = 0

        for idx in range(len(s)):
            sMap[s[idx]] = idx
            tMap[t[idx]] = idx
        
        for char in s:
            s_pos, t_pos = sMap[char], tMap[char]
            final += abs(s_pos - t_pos)
        
        return final