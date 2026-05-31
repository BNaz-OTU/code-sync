class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        visit = set()

        def dfs(index):            
            for n_index in range(len(isConnected)):
                if (isConnected[index][n_index] == 1 and (index, n_index) not in visit):
                    visit.add((index, n_index))
                    visit.add((n_index, index))
                    dfs(n_index)


        for idx in range(len(isConnected)):
            for jdx in range(len(isConnected)):
                if (isConnected[idx][jdx] == 1 and (idx, jdx) not in visit):
                    visit.add((idx, jdx))
                    visit.add((jdx, idx))
                    dfs(jdx)
                    count += 1
        
        return count