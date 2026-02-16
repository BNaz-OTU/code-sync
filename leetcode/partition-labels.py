class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # USED SOLN: https://www.youtube.com/watch?v=WQZdwxZJAhY

        dictPart = {}
        final = []

        for idx in range(len(s)):
            if (s[idx] in dictPart):
                dictPart[s[idx]] = idx
            
            else:
                dictPart[s[idx]] = idx

        print(dictPart)

        end = 0
        size = 0
        for idx in range(len(s)):
            size += 1

            if (end == 0):
                end = dictPart[s[idx]] 

            if (dictPart[s[idx]] > end):
                end = dictPart[s[idx]]

            if (idx == end):
                final.append(size)
                size = 0
                end = 0
        
        return final