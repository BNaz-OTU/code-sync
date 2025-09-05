class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # USED SOLN: https://www.youtube.com/watch?v=c4oOIi5YTE4

        N = len(code)
        res = [0] * N

        left = 0
        cur_sum = 0

        for right in range(N + abs(k)):
            cur_sum += code[right % N]

            # If we summed up to many numbers that were needed
            # remove the oldest number that was added
            if ((right - left + 1) > abs(k)):
                cur_sum -= code[left % N]
                left = (left + 1) % N
            
            # Choose wear to save the value on the final list
            if ((right - left + 1) == abs(k)):
                # If postive, map value to the left index for that current sum
                if (k > 0):
                    res[(left - 1) % N] = cur_sum
                # If negative, map value to the left index for that current sum
                elif (k < 0):
                    res[(right + 1) % N] = cur_sum
        
        return res