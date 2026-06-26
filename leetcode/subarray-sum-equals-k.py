class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        count = 0
        hashMap = {0 : 1}

        for num in nums:
            total += num

            diff = total - k

            if (diff in hashMap):
                count += hashMap[diff]
            
            if (total not in hashMap):
                hashMap[total] = 0
            
            hashMap[total] += 1
        
        return count