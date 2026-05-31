class Solution:
    def frequencySort(self, s: str) -> str:
        hashMap = {}
        final = ""

        for char in s:
            if (char not in hashMap):
                hashMap[char] = 0
            
            hashMap[char] += 1
        
        heap = []

        for key, val in hashMap.items():
            heappush(heap, [-val, key])
        
        while len(heap) > 0:
            freq, char = heappop(heap)
            final += char * (freq * -1)
        
        return final