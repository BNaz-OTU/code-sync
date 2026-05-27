class Solution:
    def frequencySort(self, s: str) -> str:
        hashMap = {}
        heap = []
        final = ""

        for char in s:
            if (char not in hashMap):
                hashMap[char] = 0
            
            hashMap[char] += 1
        
        for key in hashMap:
            heap.append([-hashMap[key], key])
        
        numChars = len(hashMap)

        heapify(heap)
        while numChars > 0:
            freq, char = heappop(heap)
            final += char * (freq * -1)
            numChars -= 1
        
        return final