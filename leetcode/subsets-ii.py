class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        final = []
        sort_nums = sorted(nums)
        
        def dfs(path, idx):
            if (idx >= len(sort_nums)):
                if (path not in final):
                    final.append(path.copy())
                return
            
            path.append(sort_nums[idx])
            dfs(path, idx + 1)

            path.pop()
            count = idx

            while count < len(nums) and sort_nums[count] == sort_nums[idx]:
                count += 1

            dfs(path, count)
        
        dfs([], 0)
        return final