class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        final = [0] * N

        curval = 0
        left = 0
        for idx in range(N + abs(k)):
            curval += code[(idx) % N]

            if (left + idx + 1 > abs(k)):
                curval -= code[left % N]
                left += 1
            
            if (idx - left + 1 == abs(k)):
                if (k > 0):
                    final[(left - 1) % N] = curval
                
                else:
                    final[(idx + 1) % N] = curval

            print(curval)


        return final