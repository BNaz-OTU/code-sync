class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        def helper(idx, count):
            if (idx == len(nums)):
                return 1
            
            res = helper(idx + 1, count)
            if not count[nums[idx] + k] and not count[nums[idx] - k]:
                count[nums[idx]] += 1
                res += helper(idx + 1, count)
                count[nums[idx]] -= 1
            
            return res
        
        return helper(0, defaultdict(int)) - 1