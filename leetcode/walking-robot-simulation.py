class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # maxX, maxY = 0, 0
        max_dist = 0
        position = [0, 0]
        count = 0
        direction = 0
        ob_set = set(map(tuple, obstacles))

        # print(-1 % 4)

        # Direction 
        # North - 0
        # East  - 1
        # Sount - 2
        # West  - 3
    
        # N E S W
        # 0 1 2 3
        # N   E  S  W  N  E  S  W N E S W N E S W N
        # -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 

        for command in commands:
            if (command == -1): # Turn Right
                count += 1
                direction = count % 4
            
            elif (command == -2): # Turn Left
                count -= 1
                direction = count % 4
                
            else:
                counter = 0
                while counter != command:
                    # Move North
                    if (direction == 0): 
                        position[1] += 1
                        if tuple((position[0], position[1])) in ob_set:
                            position[1] -= 1

                    # Move East
                    elif (direction == 1): 
                        position[0] += 1
                        if tuple((position[0], position[1])) in ob_set:
                            position[0] -= 1
                    
                    # Move South
                    elif (direction == 2): 
                        position[1] -= 1
                        if tuple((position[0], position[1])) in ob_set:
                            position[1] += 1

                    # Move West
                    else: 
                        position[0] -= 1
                        if tuple((position[0], position[1])) in ob_set:
                            position[0] += 1
                    
                    counter += 1
            
            max_dist = max(max_dist, (position[0] ** 2) + (position[1] **2))
            
            print(position)
                
        return max_dist