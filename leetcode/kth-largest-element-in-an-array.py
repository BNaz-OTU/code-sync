class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)

        opps_k = len(nums) - k

        while opps_k > 0:
            heappop(nums)
            opps_k -= 1

        return nums[0]