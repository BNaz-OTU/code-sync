class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # USED SOLN: https://www.youtube.com/watch?v=cEW05ofxhn0
        adjList = {}
        final = []

        for idx in range(numCourses):
            adjList[idx] = []
        
        for pre, crs in prerequisites:
            adjList[crs].append(pre)
        
        def dfs(crs):
            if (crs not in prereqMap):
                prereqMap[crs] = set()
                for prereq in adjList[crs]:
                    prereqMap[crs] |= dfs(prereq) # union
                prereqMap[crs].add(crs)
            return prereqMap[crs]
        
        prereqMap = {} # map crs -> hashset of indirect prereqs
        for crs in range(numCourses):
            dfs(crs)
        
        for u, v in queries:
            final.append(u in prereqMap[v])
        
        return final