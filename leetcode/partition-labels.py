class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dictLetter = {}
        final = []

        for idx, val in enumerate(s):
            dictLetter[val] = idx
        
        current = 0
        counter = 1
        
        for idx in range(len(s)):
            current = max(current, dictLetter[s[idx]])

            if (current == idx):
                final.append(counter)
                counter = 0
            
            counter += 1
        
        return final