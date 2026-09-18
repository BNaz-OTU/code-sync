class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        
        def dfs(text):
            if (len(text) > len(nums)):
                return

            if (len(text) == len(nums) and text not in nums):
                return text
            
            return dfs(text + "0") or dfs(text + "1")
        
        return dfs("")