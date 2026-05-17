class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
                    # N - 0.  E - 1.  S - 2.   W - 3
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dirIdx = 0
        posX = 0
        posY = 0
        maxDist = 0

        # Convert Obstacle array into 'set()' to get O(1) search time, better than O(n) search time in an array
        obs_set = set()
        for obsX, obsY in obstacles:
            obs_set.add((obsX, obsY))

        for command in commands:
            if (command == -1):
                dirIdx += 1
            
            elif (command == -2):
                dirIdx -= 1
            
            else:
                idx = dirIdx % 4
                for _ in range(command):
                    posX += direction[idx][0]
                    posY += direction[idx][1]

                    if ((posX, posY) in obs_set):
                        posX -= direction[idx][0]
                        posY -= direction[idx][1]
                        break

                maxDist = max(maxDist, (posX ** 2) + (posY ** 2))
        
        return maxDist