class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if (len(hand) % groupSize != 0):
            return False
        
        hand.sort()

        while len(hand) > 0:
            holderIdx = [0]

            for idx in range(1, len(hand)):
                if (len(holderIdx) == groupSize):
                    break

                diff = abs(hand[idx] - hand[holderIdx[-1]])
                if (diff > 1):
                    return False
                elif (diff == 1):
                    holderIdx.append(idx)
            
            if(len(holderIdx) != groupSize):
                return False

            for index in range(groupSize):
                rem_idx = holderIdx.pop()
                hand.pop(rem_idx)
        
        return True