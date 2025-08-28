class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # USED SOLN: https://www.youtube.com/watch?v=jfmJusJ0qKM
        stack = []
        score = 0

        for val in s:
            if (val == '('):
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + max(score * 2, 1)
        
        return score