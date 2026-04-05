class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heap.append(num * -1)
        
        heapify(heap)

        while len(heap) > (len(nums) - k + 1):
            heappop(heap)
        
        return heap[0] * -1