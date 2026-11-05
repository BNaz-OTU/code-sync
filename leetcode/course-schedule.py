class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adjList = {}
        visit = set()

        for crs in range(numCourses):
            adjList[crs] = []
        
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        def dfs(crs):
            if crs in visit:
                return False
            
            if adjList[crs] == []:
                return True
            
            visit.add(crs)

            for crs2 in adjList[crs]:
                if (dfs(crs2) == False):
                    return False
            
            visit.remove(crs)
            adjList[crs] = []
            return True

        for crs in range(numCourses):
            if (dfs(crs) == False):
                return False
        
        return True