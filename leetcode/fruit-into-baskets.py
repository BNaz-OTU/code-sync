class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        allFruit = [0] * 100001
        seen = set()
        left = 0
        maxFruit = 0
        total = 0
        
        for right in range(len(fruits)):
            rightVal = fruits[right]

            if (allFruit[rightVal] == 0):
                seen.add(rightVal)
            
            allFruit[rightVal] += 1
            total += 1

            while (len(seen) > 2):
                leftVal = fruits[left]
                allFruit[leftVal] -= 1
                total -= 1

                if (allFruit[leftVal] == 0):
                    seen.remove(leftVal)
                
                left += 1
            
            maxFruit = max(maxFruit, total)
        
        return maxFruit