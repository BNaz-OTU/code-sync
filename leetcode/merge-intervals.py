# @param {Integer[][]} intervals
# @return {Integer[][]}
def merge(intervals)
    sort_int = intervals.sort()
    final = [sort_int[0]]

    for st, ed in sort_int
        if st <= final[-1][1]
            final[-1][1] = [ed, final[-1][1]].max()
        
        else
            final.push([st, ed])
        end
        
    end

    return final

end