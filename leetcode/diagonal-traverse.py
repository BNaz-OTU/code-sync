class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        final = []
        dictIdx = {}
        val = (len(mat) - 1) + (len(mat[0]) - 1)

        for i in range(val + 1):
            dictIdx[i] = []

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                dictIdx[row + col].append(mat[row][col])
        
        for key in dictIdx:
            if (key % 2 == 0):
                for value in reversed(dictIdx[key]):
                    final.append(value)
            else:
                for value in dictIdx[key]:
                    final.append(value)
        
        return final