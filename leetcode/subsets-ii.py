class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        final = []
        nums.sort()

        def dfs(subset, idx):
            if (idx >= len(nums) or len(subset) == len(nums)):
                final.append(subset.copy())
                return 
            
            subset.append(nums[idx])
            dfs(subset, idx + 1)
            subset.pop()
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1

            dfs(subset, idx + 1)

        dfs([], 0)
        return final