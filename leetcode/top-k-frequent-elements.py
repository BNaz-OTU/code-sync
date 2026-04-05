class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashLet = {}
        heap = []
        final = []

        for num in nums:
            if (num in hashLet):
                hashLet[num] += 1
            else:
                hashLet[num] = 1
        
        print(hashLet)

        for key, val in hashLet.items():
            heap.append([val * -1, key])
        
        heapify(heap)

        while len(final) != k:
            val = heappop(heap)
            final.append(val[1])
        
        return final