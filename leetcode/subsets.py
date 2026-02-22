class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # USED SOLN: https://www.youtube.com/watch?v=REOH22Xwdkk
        
        res = []
        subset = []

        def dfs(idx):
            if (idx == len(nums)):
                res.append(subset.copy()) 
                return    

            # Decision to add number to the subset
            subset.append(nums[idx])
            dfs(idx + 1)

            # Decision NOT to add number to the subset
            subset.pop()
            dfs(idx + 1)
        
        dfs(0)
        return res