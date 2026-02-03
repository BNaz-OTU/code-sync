class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        newList = []
        final = [0] * len(nums)

        for idx in range(len(nums)):
            # print(f"Val: {nums[idx]} | Idx: {idx}")
            newList.append([nums[idx], idx]) 
        
        print(newList)

        heapify(newList)
        while k > 0:
            val = heappop(newList)
            val[0] = val[0] * multiplier
            heappush(newList, val)
            k-= 1

        print(newList) 
        while len(newList) > 0:
            update = newList.pop()
            indx = update[1]
            final[indx] = update[0]
        
        return final