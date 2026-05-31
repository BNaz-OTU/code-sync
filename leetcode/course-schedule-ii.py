class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {}
        final = []
        visit = set()
        cycle = set()

        def dfs(crs):
            if (crs in cycle):
                return False
            
            if (crs in visit):
                return True

            cycle.add(crs)
            visit.add(crs)

            for new_crs in adjList[crs]:
                if (not dfs(new_crs)):
                    return False
            
            cycle.remove(crs)
            if crs not in final:
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