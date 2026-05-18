class Solution:
    def longestValidParentheses(self, s: str) -> int:
        leftCount = 0
        rightCount = 0
        longest = 0

        # Check from left -> right
        for bracket in s:
            if (bracket == "("):
                leftCount += 1
            
            else:
                rightCount += 1
            
            if (leftCount < rightCount):
                leftCount = 0
                rightCount = 0
            
            elif (leftCount == rightCount):
                longest = max(longest, leftCount + rightCount)
        
        # Check from right -> left
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
            
            elif (leftCount == rightCount):
                longest = max(longest, leftCount + rightCount) 

        return longest