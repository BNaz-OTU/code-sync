class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # ** DIDNT USE SOLN, JUST CHECKED FOR REF: https://www.youtube.com/watch?v=UdUUnoiLkPg **
        maxCount = 0
        count = 0
        left = 0

        for idx in range(len(nums)):
            
            if (idx + 1 == k):
                print('here')
                count += nums[idx]
                avg = count / k
                maxCount = avg
            
            elif (idx < k):
                count += nums[idx]

            else:
                count -= nums[left]
                count += nums[idx]
                left += 1

                avg = count / k
                maxCount = max(maxCount, avg)
        
        return maxCount