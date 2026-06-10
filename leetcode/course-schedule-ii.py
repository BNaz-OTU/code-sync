class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {}
        final = []
        visit = set() # optimize, if we seen a course that isn't in the same course stream and know its not in a cycle we can return quickly 
        cycle = set() # if there happens to be a course cycle this set will declare it and return the loop immediately

        def dfs(crs):
            if (crs in cycle):
                return False
            
            if (crs in visit):
                return True
            
            visit.add(crs)
            cycle.add(crs)

            for new_crs in adjList[crs]:
                if (not dfs(new_crs)):
                    return False
                
            final.append(crs)
            cycle.remove(crs)
            return True

        for crs in range(numCourses):
            adjList[crs] = []
        
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        for crs in range(numCourses):
            if (not dfs(crs)):
                return []
        
        return final