class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        opps_k = len(nums) - k
        heapify(nums)

        while opps_k > 0:
            heappop(nums)
            opps_k -= 1
        
        return nums[0]

        nums = [5,6]
        opps_k = 0