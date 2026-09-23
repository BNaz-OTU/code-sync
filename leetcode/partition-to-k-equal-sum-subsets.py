class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        if (sum(nums) // k != sum(nums) / k):
            return False
        
        nums.sort()
        target = sum(nums) // k
        valid_num = [False] * len(nums)

        def dfs(idx, k, subset):
            if (k == 0):
                return True

            if (subset == target):
                return dfs(0, k - 1, 0)

            for jdx in range(idx, len(nums)):
                if (subset + nums[jdx] > target or valid_num[jdx] == True):
                    continue
                
                valid_num[jdx] = True

                if dfs(jdx + 1, k, subset + nums[jdx]):
                    return True

                valid_num[jdx] = False

                if (subset == 0):
                    return False
            
            return False
        
        return dfs(0, k, 0)