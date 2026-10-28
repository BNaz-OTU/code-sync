class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for asteroid in asteroids:
            skip = False
            while len(stack) >= 1:
                if ((stack[-1] < 0 and asteroid < 0) or (stack[-1] > 0 and asteroid > 0)):
                    # print("a", asteroid)
                    break

                elif (stack[-1] > 0 and asteroid < 0 and abs(stack[-1]) > abs(asteroid)):
                    # print("b", asteroid)
                    skip = True
                    break
                
                elif (stack[-1] > 0 and asteroid < 0 and abs(stack[-1]) < abs(asteroid)):
                    # print("c", asteroid)
                    stack.pop()
                
                elif (stack[-1] > 0 and asteroid < 0 and abs(stack[-1]) == abs(asteroid)):
                    # print("e", asteroid)
                    skip = True
                    stack.pop()
                    break
                
                else:
                    # print("d", asteroid)
                    break
            
            if (skip != True):
                stack.append(asteroid)
        
        return stack