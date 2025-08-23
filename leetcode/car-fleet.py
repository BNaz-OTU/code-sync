class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # USED SOLN: https://www.youtube.com/watch?v=Pr6T-3yB9RM
        speed_pos_pair = [[pos, spe] for pos, spe in zip(position, speed)]
        stack = []

        for p, s in sorted(speed_pos_pair)[::-1]:
            arrival_time = (target - p) / s

            if (len(stack) == 0 or stack[-1] < arrival_time):
                stack.append(arrival_time)
        
        print(sorted(speed_pos_pair))
        return len(stack)