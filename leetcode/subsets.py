class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        final = []
        temp = []
        
        def dfs(idx):
            if (idx >= len(nums)):
                final.append(temp.copy())
                return
            
            temp.append(nums[idx])
            dfs(idx + 1)
            temp.pop()
            dfs(idx + 1)

        dfs(0)
        return final