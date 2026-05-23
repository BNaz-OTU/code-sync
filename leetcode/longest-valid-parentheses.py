class Solution:
    def longestValidParentheses(self, s: str) -> int:
        leftCount = 0
        rightCount = 0
        longest = 0

        for bracket in s:
            if (bracket == "("):
                leftCount += 1
            
            else:
                rightCount += 1

            
            if (leftCount == rightCount):
                longest = max(longest, leftCount + rightCount)
            
            elif (rightCount > leftCount):
                leftCount = 0
                rightCount = 0
        
        leftCount = 0
        rightCount = 0
        for bracket in s[::-1]:
            if (bracket == "("):
                leftCount += 1
            
            else:
                rightCount += 1
            
            if (leftCount == rightCount):
                longest = max(longest, leftCount + rightCount)

            elif (rightCount < leftCount):
                leftCount = 0
                rightCount = 0
                
        return longest