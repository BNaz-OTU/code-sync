class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        visitA, visitB = set(), set()
        final = [0] * len(A)

        for idx in range(len(A)):
            visitA.add(A[idx])
            visitB.add(B[idx])
            cur = 0

            if (A[idx] == B[idx]):
                cur += 1
            else:
                if (A[idx] in visitB):
                    cur += 1
                
                if (B[idx] in visitA):
                    cur += 1
            
            if (idx > 0):
                final[idx] += cur + final[idx - 1]
            
            else:
                final[idx] = cur
        
        return final