class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # USED SOLN: https://www.youtube.com/watch?v=b1h5JJ9Sw74
        hashMap = {}
        final = []
        count = 0

        for idx in range(len(A)):
            if A[idx] in hashMap:
                hashMap[A[idx]] -= 1
            else:
                hashMap[A[idx]] = -1
            
            if B[idx] in hashMap:
                hashMap[B[idx]] += 1
            else:
                hashMap[B[idx]] = 1
            
            if hashMap[A[idx]] == 0:
                count += 1
            
            if hashMap[B[idx]] == 0:
                count += 1
            
            if A[idx] == B[idx]:
                count -= 1

            final.append(count)
        
        return final