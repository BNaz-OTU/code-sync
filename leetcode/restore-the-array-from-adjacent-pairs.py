class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # USED SOLN: https://www.youtube.com/watch?v=SGfdp6CFDrA
        
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        
        curr = None
        for u in graph:
            if len(graph[u]) == 1:
                curr = u 
                break

        ans = []
        seen = set()

        while curr != None:
            ans.append(curr)
            seen.add(curr)
            neis = graph[curr]
            curr = None

            for nei in neis:
                if (nei not in seen):
                    curr = nei

        return ans