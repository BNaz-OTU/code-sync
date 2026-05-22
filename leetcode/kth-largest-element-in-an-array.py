class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)

        opp_k = len(nums) - k

        while opp_k > 0:
            heappop(nums)
            opp_k -= 1
        
        return nums[0]