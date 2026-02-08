class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        dictIdx = []
        final = [0] * len(nums)

        for idx in range(len(nums)):
            dictIdx.append([nums[idx], idx])
        
        while k > 0:
            heapify(dictIdx)

            val = heappop(dictIdx)
            val[0] = val[0] * multiplier
            heappush(dictIdx, val)
            k -= 1
        
        while dictIdx:
            val = dictIdx.pop()
            final[val[1]] = val[0]
        
        return final