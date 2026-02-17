class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        
        max_num = max(nums)
        final = 0

        for _ in range(k):
            final += max_num 
            max_num += 1
        
        return final