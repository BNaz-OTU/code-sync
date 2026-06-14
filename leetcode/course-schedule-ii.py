class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {}
        final = []
        cycle = set()
        visit = set()

        def dfs(crs):
            if (crs in cycle):
                return False
            
            if (crs in visit):
                return True
            
            visit.add(crs)
            cycle.add(crs)

            for n_crs in adjList[crs]:
                if (not dfs(n_crs)):
                    return False
            
            cycle.remove(crs)
            final.append(crs)
            
            return True

        for crs in range(numCourses):
            adjList[crs] = []
        
        for crs, pre in prerequisites:
            adjList[crs].append(pre)

        for crs in range(numCourses):
            if (not dfs(crs)):
                return []
        
        return final