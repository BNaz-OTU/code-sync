class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sort_int = sorted(intervals)
        final = [sort_int[0]]

        for start, end in sort_int:
            prev = final[-1][1]

            if (start <= prev):
                final[-1][1] = max(prev, end)
            
            else:
                final.append([start, end])
        
        return final