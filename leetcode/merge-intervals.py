class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        final = [intervals[0]]

        for start, end in intervals[1:]:
            prev = final[-1][-1]

            if (start <= prev):
                final[-1][-1] = max(prev, end)
            
            else:
                final.append([start, end])
        
        return final