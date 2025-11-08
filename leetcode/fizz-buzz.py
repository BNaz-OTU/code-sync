class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []

        for idx in range(n):
            curr = idx + 1

            if (curr % 3 == 0 and curr % 5 == 0):
                answer.append("FizzBuzz")
            elif (curr % 3 == 0):
                answer.append("Fizz")
            elif (curr % 5 == 0):
                answer.append("Buzz")
            else:
                answer.append(str(curr))
        
        return answer