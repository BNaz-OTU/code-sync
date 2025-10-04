class Solution:
    def firstUniqChar(self, s: str) -> int:

        found = {}
        minV = None

        for idx, val in enumerate(s):
            if (val in found):
                found[val] = -1
            else:
                found[val] = idx
        
        print(found)

        for key in found:

            if (found[key] == -1):
                continue

            if minV is None:
                minV = found[key]
                
            else:
                minV = min(minV, found[key])
        
        if (minV == None):
            return -1
        else:
            return minV