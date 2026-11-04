class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        final = []
        temp = []

        def dfs(idx):
            if (idx == len(nums)):
                final.append(temp.copy())
                return
            
            temp.append(nums[idx])
            dfs(idx + 1)
            
            temp.pop()
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1

            dfs(idx + 1)
        
        dfs(0)
        return final