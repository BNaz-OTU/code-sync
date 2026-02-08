class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        final = []
        
        heapify(nums)
        while len(nums) > 0:
            # First Remove from old Array
            alice = heappop(nums)
            bob = heappop(nums)

            # Then add to new Array
            final.append(bob)
            final.append(alice)
        
        return final