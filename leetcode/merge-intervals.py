class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        new_list = [intervals[0]]

        for start, end in intervals[1:]:
            prev = new_list[-1][-1]
            if (start <= prev):
                new_list[-1][-1] = max(prev, end)
            
            else:
                new_list.append([start, end])

        return new_list