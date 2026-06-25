class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []

        total = 0
        for num in nums:
            total += num
            self.prefix.append(total)
        
        print(self.prefix)
        

    def sumRange(self, left: int, right: int) -> int:
        preRight = self.prefix[right]
        if left > 0:
            preLeft = self.prefix[left - 1]
        else:
            preLeft = 0
        
        return preRight - preLeft


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)