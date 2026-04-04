class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashNum = {}
        heap = []
        final = []

        for num in nums:
            if (num in hashNum):
                hashNum[num] += 1
            else:
                hashNum[num] = 1
        
        for key, val in hashNum.items():
            heap.append([val * -1, key])
        
        heapify(heap)
        while len(final) != k:
            val = heappop(heap)
            final.append(val[1])
        
        return final