class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # USED SOLN: https://www.youtube.com/watch?v=FZe0UqISmUw
        if (len(nums) == 0):
            return [[]]
        
        perms = self.permute(nums[1:])
        n_perm = []

        for p in perms:
            for idx in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(idx, nums[0])
                n_perm.append(p_copy)
        

        return n_perm