class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adjList = {idx:graph[idx] for idx in range(len(graph))}
        terminal = set()
        visit = set()
        cache = set()
        final = []

        def dfs(idx):
            if (idx in visit):
                return False
            
            if (idx in terminal or idx in cache):
                return True
            
            visit.add(idx)
            cache.add(idx)

            for n_idx in adjList[idx]:
                if (not dfs(n_idx)):
                    return False

            visit.remove(idx)    
            return True

        for key in adjList:
            if (adjList[key] == []):
                terminal.add(key)
        
        for idx in range(len(graph)):
            if (not dfs(idx)):
                continue
            
            final.append(idx)
        
        return final