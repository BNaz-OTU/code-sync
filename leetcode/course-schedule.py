class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashCrs = {}
        for crs in range(numCourses):
            hashCrs[crs] = []
        
        for crs, pre in prerequisites:
            hashCrs[crs].append(pre)
        
        print(hashCrs)

        def dfs(crs, visit):
            print(crs)
            if (hashCrs[crs] == []):
                return True
            
            if (crs in visit):
                return False
            
            visit.add(crs)

            for crs1 in hashCrs[crs]:
                print('here1')
                if (dfs(crs1, visit) == False):
                    return False
            hashCrs[crs] = []
            return True


        # Check all courses
        for crs in range(numCourses):
            visit = set()
            if (dfs(crs, visit)):
                continue
            else:
                return False

        return True