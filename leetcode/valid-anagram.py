class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        hashMapS = {}
        hashMapT = {}

        for idx in range(len(s)):
            if (s[idx] not in hashMapS):
                hashMapS[s[idx]] = 0
            
            hashMapS[s[idx]] += 1

            if (t[idx] not in hashMapT):
                hashMapT[t[idx]] = 0
            
            hashMapT[t[idx]] += 1

        for key in hashMapT:
            if ((key not in hashMapS) or (hashMapT[key] != hashMapS[key])):
                return False
        
        return True