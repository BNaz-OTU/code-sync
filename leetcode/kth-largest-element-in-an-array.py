class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Constraints: 
        # 1 <= k <= nums <= 10^5
        # -10^4 <= nums[i] <= 10^4
        heap = []
        opp_k = len(nums) - k

        for num in nums:
            heappush(heap, num)
        
        while opp_k > 0:
            heappop(heap)
            opp_k -= 1
        
        return heap[0]