class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashMap = {}
        visit = set()

        for idx in range(len(s)):
            if (s[idx] in visit):
                continue
            
            if (s[idx] not in hashMap):
                hashMap[s[idx]] = idx
            
            else:
                hashMap.pop(s[idx])
                visit.add(s[idx])
        
        if (len(hashMap) == 0):
            return -1

        return min(hashMap.values())