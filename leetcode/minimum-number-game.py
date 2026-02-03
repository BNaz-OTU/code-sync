class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        heapify(nums)
        while len(nums) > 0:
            # Remove Step:
            alice = heappop(nums)
            bob = heappop(nums)

            # Add Step:
            arr.append(bob)
            arr.append(alice)
        
        return arr