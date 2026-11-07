class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        dictT = {}
        dictS = {}

        for idx in range(len(s)):
            t_char = t[idx]
            s_char = s[idx]

            if (t_char not in dictT):
                dictT[t_char] = 0
            
            if (s_char not in dictS):
                dictS[s_char] = 0
            
            dictT[t_char] += 1
            dictS[s_char] += 1
        
        for key, count in dictT.items():
            if (key not in dictS or dictT[key] != dictS[key]):
                return False
        
        return True