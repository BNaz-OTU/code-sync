class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = {}
        final = []
        temp = []

        for num in nums:
            if num not in count:
                count[num] = 0
            
            count[num] += 1
        
        def dfs():
            if (len(temp) == len(nums)):
                final.append(temp.copy())
                return
            
            for key in count:
                if count[key] > 0:
                    temp.append(key)
                    count[key] -= 1

                    dfs()

                    temp.pop()
                    count[key] += 1

        dfs()
        return final