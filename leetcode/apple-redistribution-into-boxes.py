class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort()

        count = 0
        sum_apple = sum(apple)

        while sum_apple > 0:
            sum_apple -= capacity.pop()
            count += 1
        
        return count