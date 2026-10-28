class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        idx = 0

        for push in pushed:
            stack.append(push)
            while len(stack) >= 1 and idx < len(popped) and popped[idx] == stack[-1]:
                stack.pop()
                idx += 1
            
        return True if len(stack) == 0 else False