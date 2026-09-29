class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        max_size = (2 * n) - 1
        arr = [0] * max_size
        used = set()

        def backtrack(idx):
            if (idx == len(arr)):
                return True
            
            for num in reversed(range(1, n + 1)):
                if num in used:
                    continue
                
                if num > 1 and (idx + num >= len(arr) or arr[idx + num]):
                    continue
                
                used.add(num)
                arr[idx] = num
                if num > 1:
                    arr[idx + num] = num
                
                jdx = idx + 1
                while jdx < len(arr) and arr[jdx]:
                    jdx += 1
                
                if backtrack(jdx):
                    return True

                used.remove(num)
                arr[idx] = 0
                if num > 1:
                    arr[idx + num] = 0
                
            return False

        backtrack(0)
        return arr