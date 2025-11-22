class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        # sort_Alice = sorted(aliceSizes)
        sort_Bob = sorted(bobSizes)
        sumAlice = sum(aliceSizes)
        sumBob = sum(bobSizes)

        target = (sumAlice + sumBob) // 2

        # print(f"Alice Sum: {sumAlice} | Bob Sum: {sumBob}")

        # Calculate for Alice swapping with Bob
        for val in aliceSizes:
            bob_target = target - (sumAlice - val)

            # if (bob_target in bobSizes):
            #     return [val, bob_target]

            left = 0
            right = len(bobSizes) - 1

            while (left <= right):
                middle = (left + right) // 2

                if (sort_Bob[middle] == bob_target):
                    return [val, sort_Bob[middle]]
                
                elif (sort_Bob[middle] < bob_target):
                    left = middle + 1
                
                else:
                    right = middle - 1