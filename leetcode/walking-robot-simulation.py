class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        posX = 0
        posY = 0
        maxDist = 0
                    # N = 0. E = 1.   S = 2.   W = 3
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        count_dir = 0
        obs_set = set()

        # Convert obstacles into a set, to get a more efficient search time
        for ob in obstacles:
            obs_set.add((ob[0], ob[1]))

        for command in commands:
            print(posX, posY)
            if (command == -1):
                count_dir += 1
            
            elif (command == -2):
                count_dir -= 1
            
            else:
                idx = count_dir % 4

                for _ in range(command):
                    posX += direction[idx][0]
                    posY += direction[idx][1]

                    if ((posX, posY) in obs_set):
                        posX -= direction[idx][0]
                        posY -= direction[idx][1]
                        break
                
                maxDist = max(maxDist, (posX ** 2) + (posY ** 2))
        
        print(posX, posY)
        return maxDist