class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        heapify(nums)

        target = len(nums) // 2
        prev = nums[0]
        counter = 0

        while len(nums) > 0:
            val = heappop(nums)
            # print(f"Val: {val} | counter: {counter} | Prev: {prev}")
            if (counter == target):
                return val

            if (val == prev):
                counter += 1

            else:
                prev = val
                counter = 1
        
        return val