class Solution:
    def partitionString(self, s: str) -> List[str]:
        visit = set()
        final = []
        left = 0
        
        for right in range(len(s)):
            if (s[left : right + 1] in visit):
                continue
            
            else:
                visit.add(s[left : right + 1])
                final.append(s[left : right + 1])
                left = right + 1
        
        return final