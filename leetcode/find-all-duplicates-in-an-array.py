class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        visit = set()
        final = []

        for num in nums:
            if num in visit:
                final.append(num)
            else:
                visit.add(num)
        
        return final