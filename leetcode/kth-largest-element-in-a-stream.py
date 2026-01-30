class KthLargest:
    # USED SOLN: https://www.youtube.com/watch?v=hOjcdrqMoQ8
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

        # pass
        # [4,5,8,2]
        # # 3rd Largest
        # # Add 3 --- [2, 3, 4, 5, 8] -> 4
        # # Add 5 --- [2, 3, 4, 5, 5, 8] -> 5
        # # Add 10 -- [2, 3, 4, 5, 5, 8, 10] -> 5
        # # Add 9 --- [2, 3, 4, 5, 5, 8, 9, 10] -> 8
        # # Add 4 --- [2, 3, 4, 4, 5, 5, 8, 9, 10] -> 8

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if (len(self.minHeap) > self.k):
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)