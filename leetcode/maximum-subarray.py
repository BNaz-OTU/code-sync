class Solution:

    # REF SOLN: https://www.youtube.com/watch?v=5WZl3MMT0Eg
    def maxSubArray(self, nums: List[int]) -> int:
        # Setup variables
        maxSum = None
        currSum = 0

        for val in nums:
            if (currSum  < 0):
                currSum = 0

            currSum += val
            
            # In the case where it is only negative numbers, set 'maxSum' to 'currSum',
            # if this wasn't here, comparing a 'number' (currSum) and 'None' (maxSum) would break the code, 
            # if there were only negatives and 'maxSum' was '0', it would be wrong since '0' didn't appear
            # in the array
            if (maxSum is None):
                maxSum = currSum
            else:    
                maxSum = max(currSum, maxSum)
        
        return maxSum