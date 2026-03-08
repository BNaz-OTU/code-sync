class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # USED SOLN: https://www.youtube.com/watch?v=EgI5nU9etnU
        visit = set()
        hashMap = {}

        for num in range(numCourses):
            hashMap[num] = []
        
        for crs, pre in prerequisites:
            hashMap[crs].append(pre)
        
        print(hashMap)
        def dfs(crs):
            if (crs in visit):
                return False

            if (hashMap[crs] == []):
                return True
            
            visit.add(crs)
            for pre in hashMap[crs]:
               if (not dfs(pre)):
                return False
            
            visit.remove(crs)
            hashMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if (dfs(crs) == False):
                return False
            # visit = set()
        
        return True