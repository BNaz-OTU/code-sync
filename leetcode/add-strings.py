class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        # Credit: https://www.youtube.com/watch?v=q1RR8gk47Cg
        # (I watched vid once but attempted by myself after not looking at answer)

        new_sum = []
        num1_idx = len(num1) - 1
        num2_idx = len(num2) - 1
        carry = 0

        while num1_idx >= 0 or num2_idx >= 0:
            if (num1_idx < 0):
                val1 = 0

            else:
                val1 = int(num1[num1_idx])
            
            if (num2_idx < 0):
                val2 = 0

            else:
                val2 = int(num2[num2_idx])

            new_sum.append(str((carry + val1 + val2) % 10))

            carry = (carry + val1 + val2) // 10

            num1_idx -= 1
            num2_idx -= 1


        if (carry != 0):
            new_sum.append(str(carry))
        
        # flipped = new_sum[::-1]
        return "".join(new_sum[::-1])