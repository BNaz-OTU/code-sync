class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        hashS = {}
        hashT = {}

        for idx in range(len(s)):
            if (s[idx] not in hashS):
                hashS[s[idx]] = 1
            else:
                hashS[s[idx]] += 1
            
            if (t[idx] not in hashT):
                hashT[t[idx]] = 1
            else:
                hashT[t[idx]] += 1
        
        for key in hashS:
            if (key not in hashT or hashT[key] != hashS[key]):
                return False
        
        return True