class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = {}

        for num in range(len(edges)):
            adjList[num + 1] = []
        
        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)

            for val in adjList[node]:
                if (val == prev):
                    continue
                
                if (not dfs(val, node)):
                    return False
                
            return True

        for v1, v2 in edges:
            visit = set()
            adjList[v1].append(v2)
            adjList[v2].append(v1)

            if not dfs(v1, -1):
                return [v1, v2]