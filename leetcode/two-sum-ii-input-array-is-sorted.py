class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            leftVal, rightVal = numbers[left], numbers[right]
            
            if (leftVal + rightVal == target):
                return [left + 1, right + 1]
            
            elif ((leftVal + rightVal) < target):
                left += 1
            
            else:
                right -= 1