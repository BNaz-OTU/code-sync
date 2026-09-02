class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final = []

        def dfs(idx, subset):
            if (idx >= len(nums)):
                final.append(subset.copy())
                return
            
            subset.append(nums[idx])
            dfs(idx + 1, subset)

            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1

            subset.pop()
            dfs(idx + 1, subset)
        
        dfs(0, [])
        return final