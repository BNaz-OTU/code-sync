class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # DIDNT WORK 
        
        boundary = None
        count = 0

        for inval in intervals:
            if (boundary == None):
                boundary = inval

            # # Checks if there are overlaps at the start
            # elif (boundary[0] == inval[0]):
            #     print(f'Issue START: B: {boundary} | interval {inval}')
            #     count += 1
            
            # # Checks if there are overlaps at the end
            # elif (boundary[1] == inval[1]):
            #     print(f'Issue END: B: {boundary} | interval {inval}')
            #     count += 1
            
            elif (boundary[0] < inval[0] and boundary[1] > inval[1]):
                count += 1
            
            if (boundary[0] > inval[0]):
                boundary[0] = inval[0]
            
            if (boundary[1] < inval[1]):
                boundary[1] = inval[1]
        
        return count