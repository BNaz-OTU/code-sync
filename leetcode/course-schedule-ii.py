class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {}
        final = []
        cycle = set() # Detect if there is a cycle in taking courses
        visit = set() # Detect if value is already in the final list

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
            
            final.append(crs)
            cycle.remove(crs)
            return True
        
        for crs in range(numCourses):
            if (not dfs(crs)):
                return []
        
        return final