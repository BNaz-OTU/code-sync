class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        final = [0] * len(score)
        idxMap = {}

        for idx in range(len(score)):
            idxMap[score[idx]] = idx
            score[idx] = score[idx] * -1
        
        print(score)
        print(idxMap)

        heapify(score)
        count = 0

        while count < len(final):
            count += 1
            val = heappop(score) * -1 
            idxVal = idxMap[val]
            
            if (count == 1):
                final[idxVal] = "Gold Medal"
            elif (count == 2):
                final[idxVal] = "Silver Medal"
            elif (count == 3):
                final[idxVal] = "Bronze Medal"
            else:
                final[idxVal] = str(count)

        
        return final