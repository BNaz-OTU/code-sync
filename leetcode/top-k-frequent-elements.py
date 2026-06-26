class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        heap = []
        final = []

        for num in nums:
            if (num not in hashMap):
                hashMap[num] = 0

            hashMap[num] += 1
        
        for key, freq in hashMap.items():
            heappush(heap, [-freq, key])
        
        while k > 0:
            _, key = heappop(heap)
            final.append(key)

            k -= 1
        
        return final