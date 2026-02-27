class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        final = []
        subset = []
        nums.sort()

        def dfs(idx, subset):
            if (idx >= len(nums)):
                final.append(subset.copy())
                return
            
            # Include the number
            subset.append(nums[idx])
            dfs(idx + 1, subset)
            subset.pop()

            while idx < len(nums) - 1 and nums[idx] == nums[idx + 1]:
                idx += 1

            # Exclude the number
            dfs(idx + 1, subset)
        
        dfs(0, subset)
        return final