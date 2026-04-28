class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashMap = {}
        final = []

        for num in nums:
            if (num in hashMap):
                final.append(num)
            if (num not in hashMap):
                hashMap[num] = 1
        
        return final