class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashChar = {}
        visit = set()

        for idx, char in enumerate(s):
            # print(idx, char)
            if (char in visit):
                continue
            
            if (char not in hashChar):
                hashChar[char] = idx
            else:
                hashChar.pop(char)
                visit.add(char)
        
        if (len(hashChar) == 0):
            return -1

        return min(hashChar.values())