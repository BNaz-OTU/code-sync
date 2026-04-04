class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashCrs = {}
        visit = set()

        for crs in range(numCourses):
            hashCrs[crs] = []
        
        for crs, pre in prerequisites:
            hashCrs[crs].append(pre)
        
        def dfs(crs):
            if crs in visit:
                return False
            
            if (hashCrs[crs] == []):
                return True
            
            visit.add(crs)

            for crs1 in hashCrs[crs]:
                if (not dfs(crs1)):
                    return False
            
            visit.remove(crs)
            hashCrs[crs] = []
            return True
            
        
        for crs in range(numCourses):
            if (not dfs(crs)):
                return False
        
        return True