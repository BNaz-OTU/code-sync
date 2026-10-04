class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        heap = []
        final = []
        hashmap = {}

        for num in nums:
            if (num not in hashmap):
                hashmap[num] = 0
            
            hashmap[num] += 1
        
        for key, val in hashmap.items():
            heappush(heap, [-val, key])
        
        while k > 0:
            _, number = heappop(heap)
            final.append(number)
            k -= 1
        
        return final