class Solution:
    def rob(self, nums: list[int]) -> int:
        
        def helper(arr):
            arr.append(0)
            # print(f"Before: {arr}")
            for idx in range(len(arr) - 4, -1, -1):
                arr[idx] += max(arr[idx + 2], arr[idx + 3])
            
            # print(f"After: {arr}")
            return max(arr[0], arr[1])
        
        if (len(nums) < 2):
            return nums[0]

        return max(helper(nums[1:]), helper(nums[:-1]))