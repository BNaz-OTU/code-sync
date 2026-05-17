class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        for idx in range(len(nums)):
            # Convert number to a string and reverse it
            val = str(nums[idx])[::-1]

            # Add number to the array, (since its a string need to re-convert back to 'int')
            nums.append(int(val))
        
        return len(set(nums))