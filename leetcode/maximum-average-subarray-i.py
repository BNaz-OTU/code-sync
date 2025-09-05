class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        maxAvg = 0
        num_sum = 0

        for idx in range(k):
            # print(num_sum, nums[idx])
            num_sum += nums[idx]
        
        maxAvg = num_sum / k
        # print(num_sum)
        for idx in range(k, len(nums)):
            # print(f"NEW: {nums[idx]} | OLD: {nums[idx - k]}")
            num_sum += nums[idx]
            num_sum -= nums[idx - k]
            # print(maxAvg, num_sum / k)
            maxAvg = max(maxAvg, num_sum / k)
        
        return maxAvg