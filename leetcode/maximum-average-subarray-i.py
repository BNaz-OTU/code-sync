class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = 0

        for index in range(k):
            cur_sum += nums[index]
        
        maxAvg = cur_sum / k
        
        left = 0
        for right in range(k, len(nums)):
            cur_sum += nums[right]
            cur_sum -= nums[left]
            maxAvg = max(maxAvg, cur_sum / k)

            left += 1
        
        return maxAvg