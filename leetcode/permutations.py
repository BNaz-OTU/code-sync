class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for num in nums:
            temp = []
            for p in perms:
                for idx in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(idx, num)
                
                    temp.append(p_copy)
            
            perms = temp
        
        return perms