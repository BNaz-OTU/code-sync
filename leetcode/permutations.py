class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        perms = [[]]

        for num in nums:
            p = []
            for perm in perms:
                for idx in range(len(perm) + 1):
                    p_copy = perm.copy()
                    p_copy.insert(idx, num)
                    p.append(p_copy)
                
            perms = p
        
        return perms