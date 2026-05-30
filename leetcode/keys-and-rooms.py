class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        my_set = set()

        def dfs(key):
            if (key in my_set):
                return
            
            my_set.add(key)

            for new_key in rooms[key]:
                dfs(new_key)

        dfs(0)

        return len(my_set) == len(rooms)