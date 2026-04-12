class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashT = {}

        for char in t:
            if (char in hashT):
                hashT[char] += 1
            else:
                hashT[char] = 1
        
        for char in s:
            if (char in hashT):
                hashT[char] -= 1

                if (hashT[char] == 0):
                    hashT.pop(char)
            
        # print(hashT.keys())
        # # return hashT.keys()

        for key in hashT.keys():
            return key