class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        idxK = len(nums) - k
        heapify(nums)

        while idxK > 0:
            # print(idxK, heappop(nums))
            heappop(nums)
            idxK -= 1
        
        print(nums)
        return nums[0]