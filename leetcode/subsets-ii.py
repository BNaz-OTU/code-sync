class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final = []

        def dfs(path, idx):
            if (idx >= len(nums)):
                final.append(path.copy())
                return
            
            path.append(nums[idx])
            dfs(path, idx + 1)

            count = idx
            while count < len(nums) and nums[count] == nums[idx]:
                count += 1

            path.pop()
            dfs(path, count)
        
        dfs([], 0)
        return final