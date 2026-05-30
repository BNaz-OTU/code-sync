class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cycle = set()
        visit = set()
        adjList = {idx:[] for idx in range(numCourses)}
        final = []

        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        def dfs(crs):
            if (crs in cycle):
                return False
            
            if (crs in visit):
                return True
            
            cycle.add(crs)

            for new_crs in adjList[crs]:
                if (not dfs(new_crs)):
                    return False

            if (crs not in visit):
                final.append(crs)
            
            visit.add(crs)
            cycle.remove(crs)

            return True
        
        for crs in range(numCourses):
            if (not dfs(crs)):
                print(crs, final)
                return []
        
        return final
        
        print(adjList)