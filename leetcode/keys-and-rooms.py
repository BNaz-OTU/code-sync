class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visit = set()


        def dfs(key):
            if key in visit:
                return 
            
            visit.add(key)

            for nextKey in rooms[key]:
                dfs(nextKey)
        
        dfs(0)

        return len(visit) == n