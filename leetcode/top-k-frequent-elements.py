class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        heap = []
        final = []

        for num in nums:
            if (num not in hashMap):
                hashMap[num] = 0
            
            hashMap[num] += 1
        
        for key, value in hashMap.items():
            heappush(heap, [-value, key])
        
        while k > 0:
            val = heappop(heap)
            final.append(val[1])
            k -= 1
        
        return final