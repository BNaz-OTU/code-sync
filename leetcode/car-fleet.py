class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack = []
        arr = [[p, s] for p, s in zip(position, speed)]
        arr.sort()

        for pair in arr[::-1]:
            val = (target - pair[0]) / pair[1]
            stack.append(val)
            if (len(stack) >= 2 and stack[-1] <= stack[-2]):
                stack.pop()
        
        return len(stack)