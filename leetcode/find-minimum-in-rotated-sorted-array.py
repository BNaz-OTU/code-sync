class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        final = nums[0]

        idx = 0
        print(f"Starting - Left: {nums[left]} | Right: {nums[right]} | Current Minimum: {final}")
        while left <= right:
            idx += 1
            if (nums[left] < nums[right]):
                print(f"{idx}. {nums[left]} < {nums[right]} | Minimum Num: {final} & {nums[left]}")
                final = min(final, nums[left])
                break

            middle = (left + right) // 2
            final = min(final, nums[middle])

            if (nums[middle] >= nums[left]):
                print(f"{idx}. {nums[middle]} >= {nums[left]} | Minimum Num: {final}  --- Make left bigger since we are at a possible edge")
                left = middle + 1
            
            else:
                print(f"{idx}. {nums[middle]} < {nums[left]} | Minimum Num: {final}  --- Make right smaller since middle number is smaller than left number")
                right = middle - 1
        
        return final