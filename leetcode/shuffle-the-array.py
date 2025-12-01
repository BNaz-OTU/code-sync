class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0] * (2 * n)

        for idx in range(n):
            ans[idx * 2] = nums[idx]
            ans[2 * idx + 1] = nums[idx + n]
            # ans.append(nums[idx])
            # ans.append(nums[idx + n])
        
        return ans