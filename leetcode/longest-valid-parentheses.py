class Solution:
    def longestValidParentheses(self, s: str) -> int:
        leftCount, rightCount = 0, 0
        longest = 0

        for bracket in s:
            if (bracket == "("):
                leftCount += 1
            
            else:
                rightCount += 1
            
            if (leftCount < rightCount):
                leftCount, rightCount = 0, 0
            
            if (leftCount == rightCount):
                longest = max(longest, leftCount + rightCount)
        
        leftCount, rightCount = 0, 0
        for bracket in s[::-1]:
            if (bracket == "("):
                leftCount += 1
            
            else:
                rightCount += 1
            
            if (leftCount > rightCount):
                leftCount, rightCount = 0, 0
            
            if (leftCount == rightCount):
                longest = max(longest, leftCount + rightCount)
        
        return longest