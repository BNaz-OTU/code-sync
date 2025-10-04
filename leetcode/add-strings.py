class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        total = 0
        max_len = max(len(num1), len(num2))

        r_num1 = num1[::-1]
        r_num2 = num2[::-1]

        for idx in range(max_len):
            if (idx < len(num1)):
                if (idx == 0):
                    total += (ord(r_num1[-1]) - 48)
                else:
                    total += (ord(r_num1[-1]) - 48) * (10 * (idx + 1))
            
            if (idx < len(num2)):
                if (idx == 0):
                    total += (ord(r_num2[-1]) - 48)
                else:
                    total += (ord(r_num2[-1]) - 48) * (10 * (idx + 1))
        
        return str(total)