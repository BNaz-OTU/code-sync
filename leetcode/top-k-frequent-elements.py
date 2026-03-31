class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashNum = {}
        heap = []
        final = []

        for num in nums:
            if (num not in hashNum):
                hashNum[num] = 1
            else:
                hashNum[num] += 1

        print(hashNum)

        for key, value in hashNum.items():
            heap.append([value * -1, key])
        
        heapify(heap)

        while len(final) != k:
            val = heappop(heap)
            final.append(val[1])
        
        return final