# @param {Character[][]} grid
# @return {Integer}
def num_islands(grid)
    rows = grid.size()
    cols = grid[0].size()
    visit = Set.new
    count = 0

    def dfs(row, col, rows, cols, grid, visit)
        if ((row < 0 or row >= rows) or
            (col < 0 or col >= cols) or
            (grid[row][col] == "0") or
            (visit.include?([row, col])))
            return
        end
        
        visit.add([row, col])

        dfs(row + 1, col, rows, cols, grid, visit)
        dfs(row - 1, col, rows, cols, grid, visit)
        dfs(row, col + 1, rows, cols, grid, visit)
        dfs(row, col - 1, rows, cols, grid, visit)
    end

    for idx in 0...rows
        for jdx in 0...cols
            if (grid[idx][jdx] == "1" and !visit.include?([idx, jdx]))
                dfs(idx, jdx, rows, cols, grid, visit)
                count += 1
            end
        end
    end

    return count

end