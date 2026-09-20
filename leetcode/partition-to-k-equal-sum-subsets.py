class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        if (sum(nums) // k != sum(nums) / k):
            return False
        
        nums.sort(reverse=True)
        used = [False] * len(nums)
        
        target = sum(nums) // k

        def dfs(idx, k, subSetSum):
            if (k == 0):
                return True
            
            if (subSetSum == target):
                return dfs(0, k - 1, 0)
            
            for j in range(idx, len(nums)):
                if (used[j] or subSetSum + nums[j] > target):
                    continue
                
                used[j] = True

                if dfs(j + 1, k, subSetSum + nums[j]):
                    return True
                
                used[j] = False

                if (subSetSum == 0):
                    return False
            
            return False
                
        return dfs(0, k, 0)