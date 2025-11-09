class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0

        for idx in range(len(nums) - 1):
            left = idx + 1
            right = len(nums) - 1

            while left < right:
                print(f"IDX:{nums[idx]}  | LEFT: {nums[left]} | RIGHT: {nums[right]}")
                if ((nums[left] - nums[idx] > diff) or (nums[right] - nums[left] < diff)):
                    break
                elif ((nums[left]- nums[idx] == diff) and (nums[right] - nums[left] == diff)):
                    count += 1
                    break
                
                if (nums[left] - nums[idx] < diff):
                    left += 1
                elif (nums[right] - nums[left] > diff):
                    right -= 1
        
        return count