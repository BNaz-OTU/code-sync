class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []

        for idx in range(len(prices)):
            answer.append(prices[idx])
            for jdx in range(idx + 1, len(prices)):
                if (prices[jdx] <= prices[idx]):
                    updated_val = answer.pop() - prices[jdx]
                    answer.append(updated_val)
                    break
        
        return answer