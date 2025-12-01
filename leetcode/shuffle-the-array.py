class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []

        for idx in range(n):
            ans.append(nums[idx])
            ans.append(nums[idx + n])
        
        return ans