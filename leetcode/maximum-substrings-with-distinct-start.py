class Solution:
    def maxDistinct(self, s: str) -> int:
        visit = set()

        for char in s:
            visit.add(char)
        
        return len(visit)