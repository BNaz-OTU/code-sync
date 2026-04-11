class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {}
        final = []
        visit = set()
        cycle = set()

        for crs in range(numCourses):
            adjList[crs] = []
        
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        def dfs(crs):
            if (crs in cycle):
                return False
            
            if (crs in visit):
                return True
            
            visit.add(crs)
            cycle.add(crs)

            for crs1 in adjList[crs]:
                if (not dfs(crs1)):
                    return False
            
            if crs not in final:
                final.append(crs)
            cycle.remove(crs)
            return True

        
        for crs in range(numCourses):
            if (not dfs(crs)):
                return []
        
        return final