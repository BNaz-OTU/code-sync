class Solution:
    def firstUniqChar(self, s: str) -> int:
        # dictHolder = {}
        # found = set()

        found = {}
        minV = None


        for idx, val in enumerate(s):
            if (val in found):
                found[val] = len(s)
            else:
                found[val] = idx
        
        print(found)

        for key in found:
            if minV is None:
                minV = found[key]
            
            else:
                minV = min(minV, found[key])
        
        if (minV == len(s)):
            return -1
        else:
            return minV