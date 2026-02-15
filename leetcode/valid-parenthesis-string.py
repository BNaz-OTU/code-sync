class Solution:
    def checkValidString(self, s: str) -> bool:
        # USED SOLN: https://www.youtube.com/watch?v=QhPdNS143Qg

        leftMin, leftMax = 0, 0

        for val in s:
            if (val == "("):
                leftMin, leftMax = leftMin + 1, leftMax + 1
            
            elif (val == ")"):
                leftMin, leftMax = leftMin - 1, leftMax - 1
            
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            
            if (leftMax < 0):
                return False

            if (leftMin < 0):
                leftMin = 0
        
        return leftMin == 0