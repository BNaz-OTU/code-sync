class Solution:
    # USED SOLN: https://www.youtube.com/watch?v=REOH22Xwdkk

    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = []
        subset = []

        def dfs(idx):
            if (idx >= len(nums)):
                final.append(subset.copy())
                return 
            
            # Include the number
            subset.append(nums[idx])
            dfs(idx + 1)

            # Exclude the number
            subset.pop()
            dfs(idx + 1)
        
        dfs(0)
        return final