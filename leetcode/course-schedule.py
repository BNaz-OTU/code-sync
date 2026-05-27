class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        visit = set()
        for crs in range(numCourses):
            adjList[crs] = []
        
        # print(adjList)

        def dfs(crs):
            if (crs in visit):
                return False
            
            if (adjList[crs] == []):
                return True
            
            visit.add(crs)

            for new_crs in adjList[crs]:
                if (dfs(new_crs) == False):
                    return False
            
            adjList[crs] = []
            visit.remove(crs)

            return True
            
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        for crs in range(numCourses):
            if (dfs(crs) == False):
                return False
            
        return True