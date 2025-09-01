class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        temp_code = [0] * len(code)

        # print(-1 % 7)
        
        for idx in range(len(code)):
            temp_k = k
            new_val = 0

            if (k > 0):
                while (temp_k > 0):
                    mod = (idx + temp_k) % len(code)
                    temp_code[idx] += code[mod]
                    temp_k -= 1

            elif (k < 0):
                while (temp_k < 0):
                    mod = (idx + temp_k) % len(code)
                    temp_code[idx] += code[mod]
                    temp_k += 1

        return temp_code