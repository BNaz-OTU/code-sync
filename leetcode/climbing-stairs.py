class Solution:
    def climbStairs(self, n: int) -> int:
        one_step = 0
        two_step = 1

        for idx in range(n):
            temp = two_step
            two_step = one_step + two_step
            one_step = temp
        
        return two_step