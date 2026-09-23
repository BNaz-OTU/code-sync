class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        numSet = set(nums)
        n = len(nums)

        def dfs(myNum):
            if (len(myNum) > n or myNum in numSet):
                return

            if (len(myNum) == n and myNum not in numSet):
                return myNum
            
            return dfs(myNum + "1") or dfs(myNum + "0")
        
        return dfs("")