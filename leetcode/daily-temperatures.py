class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # DOESNT WORK
        answer = []

        for idx in range(len(temperatures)):
            found = False
            for jdx in range(idx + 1, len(temperatures)):
                if (temperatures[idx] < temperatures[jdx]):
                    answer.append(jdx - idx)
                    found = True
                    break
            
            if (found == False):
                answer.append(0)
        
        # print(answer)
        return answer