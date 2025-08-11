class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # WRONG
        iterate = len(dist)
        count = 0

        while (count != iterate):
            min_monster = None
            saved = None
            for idx in range(iterate):

                # If monster was already eliminated
                if (dist[idx] == 'X'):
                    continue

                # If you can't eliminate all the monsters
                elif (dist[idx] <= 0):
                    return count
                
                # Determine the closest monster
                elif ((min_monster == None) or (dist[idx] - speed[idx] < min_monster)):
                    min_monster = dist[idx] - speed[idx]
                    saved = idx
                
                if (dist[idx] != 'X'):
                    dist[idx] -= speed[idx]
            
            
            dist[saved] = 'X'
            count += 1   
            print(dist) 

        return count