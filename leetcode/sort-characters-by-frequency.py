class Solution:
    # ALT METHOD: https://www.youtube.com/watch?v=OXdXc9HTrIg
    def frequencySort(self, s: str) -> str:
        dictChar = {}
        helperList = []
        final = ""

        for char in s:
            if (char in dictChar):
                dictChar[char] += 1
            else:
                dictChar[char] = 1
        
        print(dictChar)

        for key, val in dictChar.items():
            helperList.append([val, key])

        heapify(helperList)
        while len(helperList) > 0:
            val = heappop(helperList)
            newStr = val[1] * val[0]
            final += newStr
        
        return final[::-1]