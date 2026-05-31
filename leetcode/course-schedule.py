class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        visit = set()

        def dfs(crs):
            if (crs in visit):
                return False
            
            if (adjList[crs] == []):
                return True

            visit.add(crs)

            for new_crs in adjList[crs]:
                if (not dfs(new_crs)):
                    return False
            
            visit.remove(crs)
            adjList[crs] = []
            return True

        for crs in range(numCourses):
            adjList[crs] = []
        
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        for crs in range(numCourses):
            if (not dfs(crs)):
                return False
        
        return True