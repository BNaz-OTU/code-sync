class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        final = []
        tempList = []

        def dfs(idx):
            if (idx == len(nums)):
                final.append(tempList.copy())
                return
            
            tempList.append(nums[idx])
            dfs(idx + 1)
            
            tempList.pop()
            dfs(idx + 1)
        
        dfs(0)
        return final