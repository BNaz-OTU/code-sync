class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        heap = []
        final = []

        for num in nums:
            if (num not in hashMap):
                hashMap[num] = 0
            
            hashMap[num] += 1
        
        for val, freq in hashMap.items():
            heappush(heap, [-freq, val])
        

        while k > 0:
            _, val = heappop(heap)
            final.append(val)
            k -= 1     
        
        return final