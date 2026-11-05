class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.heap = []
        self.capacity = k

        for num in nums:
            heappush(self.heap, num)

            if len(self.heap) > k:
                heappop(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap, val)

        if (len(self.heap) > self.capacity):
            heappop(self.heap)
        
        return self.heap[0]
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)