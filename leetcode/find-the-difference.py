class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashS = {}

        for char in s:
            if (char not in hashS):
                hashS[char] = 0
            
            hashS[char] += 1

        for char in t:
            if (char not in hashS):
                return char

            else:
                hashS[char] -= 1

                if (hashS[char] == 0):
                    hashS.pop(char)