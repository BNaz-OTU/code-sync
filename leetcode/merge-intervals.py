class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sort_int = sorted(intervals)
        final = [sort_int[0]]

        for start, end in sort_int[1:]:
            prev = final[-1][1]

            if (prev >= start):
                if (prev < end):
                    final[-1][1] = end
            
            else:
                final.append([start, end])
        
        return final