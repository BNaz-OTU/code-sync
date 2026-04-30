class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        [1, 1, 2, 6, 24]
        [24, 24, 12, 4, 1]

        arr1 = [1] * (len(nums) + 1)
        arr2 = [1] * (len(nums) + 1)
        final = []

        count = 0
        for idx in range(len(nums)):
            count -= 1
            arr1[idx + 1] = nums[idx] * arr1[idx]
            arr2[idx + 1] = nums[count] * arr2[idx]

        r_arr2 = arr2[::-1]
        for idx in range(len(arr1) - 1):
            final.append(arr1[idx] * r_arr2[idx + 1])
        
        return final
        
        
        # for idx in range(len(nums), -1, -1):
        #     arr2[idx + 1] = 
        #     print(idx)
        
        print(arr1)
        print(arr2)