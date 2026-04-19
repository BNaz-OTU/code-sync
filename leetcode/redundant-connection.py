class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = {}

        for num in range(len(edges)):
            adjList[num + 1] = []
        
        def dfs(curNum, prevNum):
            if curNum in visit:
                return False
            
            visit.add(curNum)

            for val in adjList[curNum]:
                if (val == prevNum):
                    continue
                
                if (not dfs(val, curNum)):
                    return False
            
            return True
            
        for v1, v2 in edges:
            visit = set()
            adjList[v1].append(v2)
            adjList[v2].append(v1)
            if (not dfs(v1, 0)):
                return [v1, v2]