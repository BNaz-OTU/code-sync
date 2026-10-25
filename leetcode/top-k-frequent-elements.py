class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}
        final = []
        
        for num in nums:
            if (num not in hashmap):
                hashmap[num] = 0
            
            hashmap[num] += 1
        
        heap = []
        for key, val in hashmap.items():
            heappush(heap, [-val, key])
        
        while k > 0:
            _, key = heappop(heap)
            final.append(key)
            k -= 1
        
        return final