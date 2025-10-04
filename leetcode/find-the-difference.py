class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # The Hashmap Method
        
        dictS = {}
        dictT = {}

        for val in t:
            if (val in dictT):
                dictT[val] += 1
            else:
                dictT[val] = 1
        
        for val in s:
            if (val in dictS):
                dictS[val] += 1
            else:
                dictS[val] = 1
        
        for key in dictT:
            if (key not in dictS):
                return key
            
            elif (dictS[key] != dictT[key]):
                return key