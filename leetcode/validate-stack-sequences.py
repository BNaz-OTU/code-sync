class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        pop_idx = 0
        for num in pushed:
            stack.append(num)

            while (len(stack) > 0 and stack[-1] == popped[pop_idx]):
                stack.pop()
                pop_idx += 1
        
        return True if len(stack) == 0 else False