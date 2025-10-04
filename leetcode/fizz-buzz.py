class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for idx in range(1, n + 1):
            if (idx % 3 == 0 and idx % 5 == 0):
                answer.append("FizzBuzz")
            
            elif (idx % 3 == 0):
                answer.append("Fizz")
            
            elif (idx % 5 == 0):
                answer.append("Buzz")
            
            else:
                answer.append(str(idx))
        
        return answer