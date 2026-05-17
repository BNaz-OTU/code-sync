class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest = 0

        leftCount = 0
        rightCount = 0

        for bracket in s:
            if (bracket == "("):
                leftCount += 1
            
            else:
                rightCount += 1
            
            if (rightCount > leftCount):
                leftCount = 0
                rightCount = 0
            
            if (rightCount == leftCount):
                longest = max(longest, leftCount + rightCount)
        
        leftCount = 0
        rightCount = 0

        for bracket in s[::-1]:
            if (bracket == "("):
                leftCount += 1
            
            else:
                rightCount += 1
            
            if (leftCount > rightCount):
                leftCount = 0
                rightCount = 0
            
            if (leftCount == rightCount):
                longest = max(longest, rightCount + leftCount)
        
        return longest