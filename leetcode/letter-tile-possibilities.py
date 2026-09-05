class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)


        def dfs():
            final = 0
            
            for c in count:
                if count[c] > 0:
                    count[c] -= 1
                    final += 1
                    final += dfs()
                    count[c] += 1
            
            return final

        return dfs()