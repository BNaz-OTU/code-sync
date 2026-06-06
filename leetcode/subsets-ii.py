class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        final = []
        sort_nums = sorted(nums)
        def dfs(path, idx):
            if (idx >= len(sort_nums)):
                final.append(path.copy())
                return
            
            path.append(sort_nums[idx])
            dfs(path, idx + 1)

            count = idx
            while count < len(sort_nums) and sort_nums[idx] == sort_nums[count]:
                count += 1
            
            path.pop()
            dfs(path, count)

        dfs([], 0)
        return final