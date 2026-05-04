class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sort_int = sorted(intervals)
        final = [sort_int[0]]
        
        for start, end in sort_int[1:]:
            lastEnd = final[-1][1]

            if (start <= lastEnd):
                final[-1][1] = max(lastEnd, end)
            
            else:
                final.append([start, end])
        
        return final