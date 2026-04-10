class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashCrs = {}

        for idx in range(numCourses):
            hashCrs[idx] = []
        
        for crs, pre in prerequisites:
            hashCrs[crs].append(pre)
        
        visit = set()
        cycle = set()
        final = []
        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visit:
                return True
            
            cycle.add(crs)
            
            for crs1 in hashCrs[crs]:
                if (not dfs(crs1)):
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            final.append(crs)
            return True
        
        for crs in range(numCourses):
            if (not dfs(crs)):
                return []
        
        return final