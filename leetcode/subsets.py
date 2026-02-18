class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # USED SOLN: https://www.youtube.com/watch?v=REOH22Xwdkk

        res = []
        subset = []

        def dfs(idx):
            if (idx >= len(nums)):
                res.append(subset.copy())
                return
            
            # decision to include nums[idx]
            subset.append(nums[idx])
            dfs(idx + 1)

            # decision NOT to include nums[idx]
            subset.pop()
            dfs(idx + 1)
        
        dfs(0)
        return res