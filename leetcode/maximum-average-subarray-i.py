class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_total = 0
        max_avg = 0

        for idx in range(k):
            cur_total += nums[idx]
        
        print(cur_total)
        max_avg = round(cur_total / k, 5)
        print(max_avg)

        for jdx in range(k, len(nums)):
            cur_total -= nums[jdx - k]
            cur_total += nums[jdx]
            max_avg = round(max(max_avg, cur_total / k), 5)
    
        return max_avg