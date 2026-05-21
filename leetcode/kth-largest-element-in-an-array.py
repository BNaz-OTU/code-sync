class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heap.append(-num)
        
        heapify(heap)

        val = 0
        while k > 0:
            val = heappop(heap)
            k -= 1
        
        return val * -1