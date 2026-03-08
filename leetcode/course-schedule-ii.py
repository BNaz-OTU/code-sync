class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashMap = {}
        visit = set()
        final = []

        for num in range(numCourses):
            hashMap[num] = []

        for crs, pre in prerequisites:
            hashMap[crs].append(pre)
        
        def dfs(crs):
            if (crs in visit):
                return False
            
            if (hashMap[crs] == []):
                if (crs not in final):
                    final.append(crs)
                return True
            
            visit.add(crs)
            for pre in hashMap[crs]:
                if (not dfs(pre)): 
                    return False
            visit.remove(crs)

            if (crs not in final):
                final.append(crs)
            hashMap[crs] = []
            return True

            
        for crs in range(numCourses):
            if (not dfs(crs)):
                return []

        return final