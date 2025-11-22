class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumAlice = sum(aliceSizes)
        sumBob = sum(bobSizes)

        target = (sumAlice + sumBob) // 2

        print(f"Alice Sum: {sumAlice} | Bob Sum: {sumBob}")

        # Calculate for Alice swapping with Bob
        for val in aliceSizes:
            bob_target = target - (sumAlice - val)

            if (bob_target in bobSizes):
                return [val, bob_target]

            # left = 0
            # right = len(bobSizes) - 1

            # while (left <= right):
            #     middle = (left + right) // 2

            #     if (bobSizes[middle] == bob_target):
            #         return [val, bobSizes[middle]]
                
            #     elif (bobSizes[middle] < bob_target):
            #         left = middle + 1
                
            #     else:
            #         right = middle - 1