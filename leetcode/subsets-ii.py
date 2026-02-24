class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        final = []
        subset = []
        nums.sort()

        def dfs(idx, subset):
            if (idx >= len(nums) and subset not in final):
                final.append(subset.copy())
                return 

            if (idx >= len(nums)):
                return 
            
            # Add Number
            subset.append(nums[idx])
            dfs(idx + 1, subset)

            # Don't Add Number
            subset.pop()
            dfs(idx + 1, subset)
        
        dfs(0, subset)
        return final