class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sort_i = sorted(intervals)

        final = [sort_i[0]]

        for start, end in sort_i[1:]:
            prev = final[-1][1]

            if (start <= prev):
                if (end > prev):
                    final[-1][1] = end
            else:
                final.append([start, end])
        
        return final