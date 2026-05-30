class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visit = set()
        count = 0

        def dfs(index):
            for jndex in range(len(isConnected[index])):
                if (isConnected[index][jndex] == 1 and (index, jndex) not in visit):
                    visit.add((index, jndex))
                    visit.add((jndex, index))
                    dfs(jndex)

        for idx in range(len(isConnected)):
            for jdx in range(len(isConnected[idx])):
                if (isConnected[idx][jdx] == 1 and (idx, jdx) not in visit):
                    visit.add((idx, jdx))
                    visit.add((jdx, idx))
                    dfs(jdx)
                    count += 1

        return count