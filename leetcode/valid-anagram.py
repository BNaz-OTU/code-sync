class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}

        if (len(s) != len(t)):
            return False

        for idx in range(len(s)):
            if (s[idx] in hashS):
                hashS[s[idx]] += 1
            else:
                hashS[s[idx]] = 1
            
            if (t[idx] in hashT):
                hashT[t[idx]] += 1
            else:
                hashT[t[idx]] = 1
        
        for key in hashS:
            if (key not in hashT or hashS[key] != hashT[key]):
                return False
        return True