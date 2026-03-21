# OPTIMAL SOLN: https://leetcode.com/problems/find-the-number-of-good-pairs-i/solutions/5668094/simple-onm-python-solution-beginner-frie-9oe0
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:

        key_map = defaultdict(int) # using a default dict for creating a dict for the function type int
        
        # initialising the key values for default dict
        for i in nums2:
            key_map[i*k] += 1
        
        count = 0 

        for num in nums1:
            for key in key_map:
                if num % key == 0:
                    count += key_map[key] # for the case when the numbers in nums2 are repeated 
        return count