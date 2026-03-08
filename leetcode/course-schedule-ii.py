class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashMap = {}
        cycle = set() # Used to detect if there is a cycle/forever loop of taking courses
        visit = set() # Unlike cycle this is used to determine if I've already checked a given course and prevents duplicate courses from 
                      # appearing in the final output
        final = []

        for num in range(numCourses):
            hashMap[num] = []

        for crs, pre in prerequisites:
            hashMap[crs].append(pre)
        
        def dfs(crs):
            if (crs in cycle):
                return False

            if (crs in visit):
                return True
            
            cycle.add(crs)
            for pre in hashMap[crs]:
                if (not dfs(pre)): 
                    return False

            cycle.remove(crs)
            visit.add(crs)
            final.append(crs)
            return True

            
        for crs in range(numCourses):
            if (dfs(crs) == False):
                return []

        return final