class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0

        setNum = set(nums)
        maxCount = 1

        for num in setNum:
            if ((num - 1) not in setNum):   # This will locate the lowest number to start 
                count = 0                   # searching from, if there was [1, 2, 3, 4], we want to start at 1 because checking the other numbers is a waste of time since you can find a longer sequence at starting at 1
                while (num + count) in setNum:
                    count += 1

                maxCount = max(count, maxCount)
        
        return maxCount