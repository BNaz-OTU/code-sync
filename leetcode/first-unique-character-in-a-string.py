class Solution:
    def firstUniqChar(self, s: str) -> int:
        visit = set()
        hashS = {}

        for idx, char in enumerate(s):
            if (char in visit):
                continue

            if (char not in hashS):
                hashS[char] = idx
            else:
                visit.add(char)
                hashS.pop(char)
        
        if (len(hashS) == 0):
            return -1

        return min(hashS.values())