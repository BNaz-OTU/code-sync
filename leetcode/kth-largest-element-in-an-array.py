class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        opposite_k = len(nums) - k

        heapify(nums)

        while opposite_k > 0:
            heappop(nums)
            opposite_k -= 1
        
        return nums[0]