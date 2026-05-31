class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set()
        count = 0

        def dfs(key):
            nonlocal count
            visit.add(key)
            count += 1

            for new_key in rooms[key]:
                if (new_key not in visit):
                    dfs(new_key)
        
        dfs(0)

        return count == len(rooms)