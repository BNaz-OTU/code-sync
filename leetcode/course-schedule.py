class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        visit = set()

        for num in range(numCourses):
            adjList[num] = []
        
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        

        def dfs(crs):
            if (adjList[crs] == []):
                return True
            
            if (crs in visit):
                return False
            
            visit.add(crs)

            for crs1 in adjList[crs]:
                if (not dfs(crs1)):
                    return False
            
            visit.remove(crs)
            adjList[crs] = []
            return True

        for crs in range(numCourses):
            if (not dfs(crs)):
                return False
        
        return True