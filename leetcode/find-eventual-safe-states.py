class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        final = []
        terminal_set = set() 
        visit = set()
        adjList = {idx:graph[idx] for idx in range(len(graph))}

        def dfs(key):
            if (key in visit):
                return False
            
            if (adjList[key] == [] or key in terminal_set):
                terminal_set.add(key)
                return True
            
            visit.add(key)
            
            for sub_key in adjList[key]:
                if (not dfs(sub_key)):
                    return False
            
            visit.remove(key)
            terminal_set.add(key)
            return True
            
        for node in range(len(graph)):
            if (dfs(node)):
                final.append(node)

        return final