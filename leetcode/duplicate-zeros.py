class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # USED SOLN: https://www.youtube.com/watch?v=x-dfV08jAYw

        zeroCounter = 0

        for num in arr:
            if (num == 0):
                zeroCounter += 1
        
        jdx = len(arr) - 1 + zeroCounter
        idx = len(arr) - 1

        while (idx != jdx):
            if (jdx < len(arr)):
                arr[jdx] = arr[idx]
                
            jdx -= 1

            if (arr[idx] == 0):
                if (jdx < len(arr)):
                    arr[jdx] = arr[idx]
                jdx -= 1
            
            idx -= 1