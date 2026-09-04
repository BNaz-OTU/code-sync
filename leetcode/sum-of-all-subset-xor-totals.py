class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        final = []
        finalSum = 0
        
        def dfs(idx, temp):
            if (idx >= len(nums) or len(temp) == len(nums)):
                tempSum = 0
                if (len(temp) == 1):
                    tempSum += temp[0]
                
                else:
                    tempSum = 0
                    for val in temp:
                        tempSum ^= val
                    
                final.append(tempSum)
                return
            
            temp.append(nums[idx])
            dfs(idx + 1, temp)

            temp.pop()
            dfs(idx + 1, temp)
        
        dfs(0, [])
        return sum(final)