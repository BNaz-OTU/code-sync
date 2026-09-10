class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = {}
        # final = 0

        for tile in tiles:
            if tile not in count:
                count[tile] = 0
            
            count[tile] += 1
        
        def dfs():
            final = 0
            
            for key in count:
                if count[key] > 0:
                    count[key] -= 1
                    final += 1
                    final += dfs()
                    count[key] += 1
            
            return final

        return dfs()