class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        final = [0] * len(temperatures)
        stackIdx = []

        for idx in range(len(temperatures)):
            while (len(stackIdx) >= 1 and temperatures[idx] > temperatures[stackIdx[-1]]):
                s_idx = stackIdx.pop()
                final[s_idx] = idx - s_idx
            
            stackIdx.append(idx)
        
        return final