class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)
        heap = []
        final = []

        for num in nums:
            hashMap[num] += 1
        
        for key in hashMap:
            heappush(heap, [-hashMap[key], key])
        
        while k > 0:
            val = heappop(heap)
            final.append(val[1])
            k -= 1
        
        return final