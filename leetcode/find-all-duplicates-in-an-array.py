class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        visit = set()
        final = []

        for val in nums:
            if val in visit:
                final.append(val)
            else:
                visit.add(val)
        
        return final