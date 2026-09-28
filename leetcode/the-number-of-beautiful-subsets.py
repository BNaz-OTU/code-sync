class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        count = 0

        def backtrack(idx, hashmap):
            nonlocal count
            count += 1

            if (idx == len(nums)):
                return 
            
            for jdx in range(idx, len(nums)):
                less_k = nums[jdx] - k
                more_k = nums[jdx] + k

                if ((less_k in hashmap and hashmap[less_k] >= 1) or (more_k in hashmap and hashmap[more_k] >= 1)):
                    continue
                
                if nums[jdx] not in hashmap:
                    hashmap[nums[jdx]] = 0
                
                hashmap[nums[jdx]] += 1
                backtrack(jdx + 1, hashmap)
                hashmap[nums[jdx]] -= 1
        
        backtrack(0, dict())
        return count - 1