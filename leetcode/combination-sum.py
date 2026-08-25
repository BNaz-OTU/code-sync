class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final = []

        def getSum(idx, curList):
            # print(idx, curList)
            if (sum(curList) == target):
                final.append(curList.copy())
                return
            
            if (sum(curList) > target or idx >= len(candidates)):
                return

            curList.append(candidates[idx])
            getSum(idx, curList)

            curList.pop()
            getSum(idx + 1, curList)

        getSum(0, [])
        return final