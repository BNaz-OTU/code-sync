class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        final = []

        def getCombs(num, curComb):
            if (len(curComb) == k):
                final.append(curComb.copy())
                return
            
            if (num > n):
                return

            for n_num in range(num, n + 1):
                curComb.append(n_num)
                getCombs(n_num + 1, curComb)
                curComb.pop()
                # getCombs(n_num + 1, curComb)

        getCombs(1, [])
        return final