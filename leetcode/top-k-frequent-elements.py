class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        final = []
        hashMap = {}
        heap = []

        for num in nums:
            if (num not in hashMap):
                hashMap[num] = 0
            
            hashMap[num] += 1
        
        for value, freq in hashMap.items():
            heappush(heap, [-freq, value])
        
        while k > 0:
            _, val = heappop(heap)
            final.append(val)
            k -= 1
        
        return final