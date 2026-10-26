class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rowDict = {idx : set() for idx in range(len(board))}
        colDict = {idx : set() for idx in range(len(board))}
        boxDict = {}

        for idx in range(len(board)):
            for jdx in range(len(board)):
                boxDict[(idx // 3, jdx // 3)] = set()

        for idx in range(9):
            for jdx in range(9):
                val = board[idx][jdx]

                if val == ".":
                    continue

                if (val in rowDict[idx] or 
                    val in colDict[jdx] or 
                    val in boxDict[(idx // 3, jdx // 3)]):

                    # print(f"Row: {idx} | Col: {jdx} | Val: {board[idx][jdx]}")
                    # print(rowDict[idx])
                    # print(colDict[jdx])
                    # print(boxDict[(idx // 3, jdx // 3)])
                    return False
                
                rowDict[idx].add(val)
                colDict[jdx].add(val)
                boxDict[(idx // 3, jdx // 3)].add(val)
        
        return True