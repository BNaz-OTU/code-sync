class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        final = 0
        
        def dfs(idx, perms):
            nonlocal final
            if (idx == len(nums)):
                tempVal = 0

                for val in perms:
                    tempVal ^= val
                
                final += tempVal
                return 
            
            perms.append(nums[idx])
            dfs(idx + 1, perms)
            perms.pop()
            dfs(idx + 1, perms)
        
        dfs(0, [])
        return final