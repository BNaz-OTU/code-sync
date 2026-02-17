class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if (len(hand) % groupSize != 0):
            return False
        
        hand.sort()

        while len(hand) > 0:
            holder_idx = []
            holder_idx.append(0)

            for idx in range(1, len(hand)):
                if (len(holder_idx) == groupSize):
                    break

                prev = hand[holder_idx[-1]]
                curr = hand[idx]
                # DEBUG
                # print(f"Prev: {prev} | Curr: {curr} | Difference: {curr - prev} | holder: {holder_idx}")

                if (curr - prev == 1):
                    holder_idx.append(idx)
                elif (prev == curr):
                    continue
                else:
                    return False
                
            # In the event many of the values in hand are the same EX: [3, 3, 3], return False because its not consecutively increasing
            if (len(holder_idx) != groupSize):
                return False

            for val in reversed(holder_idx):
                hand.pop(val)
        
        return True