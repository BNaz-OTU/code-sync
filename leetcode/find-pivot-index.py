class Solution:
    def queryPrefix(self, prefix, left, right):
        preRight = prefix[right]

        if left > 0:
            preLeft = prefix[left - 1]
        
        else:
            preLeft = 0
        
        return preRight - preLeft


    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []

        total = 0
        for num in nums:
            total += num
            prefix.append(total)
        
        left = 0
        right = len(nums) -1 

        for idx in range(len(nums)):
            leftSide = self.queryPrefix(prefix, left, idx)
            rightSide = self.queryPrefix(prefix, idx, right)

            if (leftSide == rightSide):
                return idx

        return -1