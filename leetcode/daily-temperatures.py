class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        final = [0] * len(temperatures)
        stack = []

        for idx in range(len(temperatures)):
            while (len(stack) > 0 and temperatures[idx] > temperatures[stack[-1]]):
                end_stack_idx = stack.pop()
                final[end_stack_idx] = idx - end_stack_idx
            
            stack.append(idx)

        return final